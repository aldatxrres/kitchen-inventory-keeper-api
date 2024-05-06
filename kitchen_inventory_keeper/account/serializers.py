from rest_framework import serializers
from djoser.serializers import (
    UserSerializer,
    UserCreateSerializer as BaseUserRegistrationSerializer,
    UserCreatePasswordRetypeSerializer,
)
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreatePasswordRetypeSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "created_at",
            "updated_at"
        )

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "groups",
            "accepted_policy",
            "last_login",
            "created_at",
            "updated_at",
        )