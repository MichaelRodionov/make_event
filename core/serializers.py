from typing import Any, Type

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from core.models import User


# ----------------------------------------------------------------
# user serializer
class UserRegSerializer(serializers.ModelSerializer):
    """
    User registration serializer

    Attrs:
        - email: user's email
        - password: current user's password
        - password_repeat: repeat of current password
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True,
    )
    password_repeat = serializers.CharField(
        write_only=True,
    )

    def validate(self, attrs) -> Any:
        """
        Redefined method to validate incoming data

        Params:
            - validated_data: dictionary with validated data of Board entity

        Returns:
            - attrs: dictionary with data

        Raises:
            - ValidationError (in case of user already exist or password repeat is wrong or no password_repeat data)
        """
        password_repeat = attrs.pop('password_repeat')
        if User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError('User with this email already exists')
        elif not password_repeat:
            raise serializers.ValidationError('Need password repeat')
        elif attrs.get('password') != password_repeat:
            raise serializers.ValidationError('Password mismatch')
        validate_password(attrs.get('password'))
        return attrs

    class Meta:
        model: Type[User] = User
        fields: list = ['id', 'email', 'password', 'password_repeat']


class UserAuthSerializer(serializers.ModelSerializer):
    """
    User authentication serializer

    Attrs:
        - email: user's email
        - password: current user's password
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True,
    )

    def validate(self, attrs) -> Any:
        """
        Redefined method to validate incoming data

        Params:
            - validated_data: dictionary with validated data of Board entity

        Returns:
            - attrs: dictionary with data

        Raises:
            - ValidationError (in case of user does not exist or invalid password)
        """
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
        model: Type[User] = User
        fields: str = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Default user serializer
    """
    class Meta:
        model: Type[User] = User
        fields: list = ['id', 'email']
