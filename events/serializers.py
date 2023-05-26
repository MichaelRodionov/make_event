from typing import Type

from rest_framework import serializers

from events.models import Event
from organizations.models import Organization
from organizations.serializers import OrgListSerializer


# ----------------------------------------------------------------
# organization serializers
class EventCreateSerializer(serializers.ModelSerializer):
    """
    Event create serializer

    Attrs:
        - organizations: related organizations
        - date: formatted datetime field
    """
    organizations = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Organization.objects.all()
    )
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model: Type[Event] = Event
        fields: str = '__all__'


class EventSerializer(serializers.ModelSerializer):
    """
    Event default serializer

    Attrs:
        - organizations: related organizations
        - date: formatted datetime field
    """
    organizations = OrgListSerializer(many=True)
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model: Type[Event] = Event
        fields: list = ['id', 'title', 'description', 'date', 'organizations', 'image']
