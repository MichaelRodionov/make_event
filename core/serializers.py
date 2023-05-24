from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from core.models import User


# ----------------------------------------------------------------
# user serializer
class UserRegSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True,
    )
    password_repeat = serializers.CharField(
        write_only=True,
    )

    def validate(self, attrs):
        password_repeat = attrs.pop('password_repeat')
        if not password_repeat:
            raise serializers.ValidationError('Need password repeat')
        elif attrs.get('password') != password_repeat:
            raise serializers.ValidationError('Password mismatch')
        validate_password(attrs.get('password'))
        return attrs

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'password_repeat']


class UserAuthSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True,
    )

    def validate(self, attrs):
        email, password = attrs.get('email'), attrs.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('User does not exist')
        if user.password != password:
            raise serializers.ValidationError('Invalid password')
        attrs['user'] = user
        return attrs

    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
