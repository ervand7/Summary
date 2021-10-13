from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer для User."""

    class Meta:
        model = User
        # это те поля юзера, которые будут сериализовываться. Все поля юзеров лежат в auth_user
        fields = ('id', 'username')
