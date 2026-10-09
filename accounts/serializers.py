from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]


    def validate_password(self, value):
        if len(value)<8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long."
            )
        print(value)
        return value