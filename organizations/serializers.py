from typing import Type, Any

from rest_framework import serializers

from core.models import User
from core.serializers import UserSerializer
from organizations.models import Organization


# ----------------------------------------------------------------
# organization serializers
class OrgCreateSerializer(serializers.ModelSerializer):
    """
    Organization create serializer
    """
    def create(self, validated_data) -> Any:
        """
        Redefined create method to set organization to user
        """
        instance = Organization.objects.create(**validated_data)
        user = User.objects.filter(id=self.context['request'].user.id).first()
        user.organization = instance
        user.save()
        return instance

    class Meta:
        model: Type[Organization] = Organization
        fields: str = '__all__'


class OrgListSerializer(serializers.ModelSerializer):
    """
    Organization list serializer

    Attrs:
        - user: related user
        - full_address: field with united address and postcode
    """
    user = UserSerializer(source='users', many=True)
    full_address = serializers.SerializerMethodField()

    def get_full_address(self, org) -> str:
        """
        Method to define full_address
        """
        return f'{org.address}, {org.postcode}'

    class Meta:
        model: Type[Organization] = Organization
        exclude: list = ['address', 'postcode']
