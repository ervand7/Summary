from django.contrib.auth.models import User
from rest_framework import serializers
from .consts import *

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""
    # заполняем обязательный подкласс Meta
    class Meta:
        model = User
        # это те поля creator'а, которые будут сериализовываться. Все поля юзеров лежат в auth_user
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""
    # мы говорим, что поле creator будет принимать значение UserSerializer
    creator = UserSerializer(read_only=True, )  # read_only=True означает, что
    # мы это поле не трогаем, так как оно уже звсереализованно другим сериализатором

    class Meta:
        model = Advertisement
        fields = (
            'id', 'title', 'description', 'creator', 'status', 'created_at', 'is_draft',
        )

    def validate(self, attrs):
        """
        Метод для валидации. Вызывается при создании и обновлении.
        Здесь мы валидируем максимально допустимое
        кол-во объявлений, которые могут быть у одного пользователя (10).

        Внимание! Название этого метода зарезервированно!
        """
        creator: User = self.context["request"].user
        attrs["creator"]: User = creator
        creator_id: int = attrs["creator"].id
        if attrs['status'] == OPEN:
            user_open_advertisements: int = Advertisement.objects.filter(
                creator_id=creator_id, status=OPEN
            ).count()
            if user_open_advertisements == 10:
                raise serializers.ValidationError(
                    'Нельзя иметь более 10 объявлений со статусом <OPEN>!'
                )
        return attrs
