from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Car


class CarSerializerFromModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'  # __all__ означает, что все поля будут обязательными. Мы могли бы прописать
        # только ('name',) - в таком случае у нас было бы только одно обязательное поле

    # =========================================================================================
    # =========================================================================================
    # =============================== В А Л И Д А Ц И Я ====================================
    # ВНИМАНИЕ! Название валидирующей функции должно начинаться с validate_
    def validate_name(self, name: str) -> str:  # name - это значение, которое придет с фронтенда
        if len(name) < 3:
            # POST http://localhost:4000/api/v1/cars/ with body: {"name": "vv", "amount":  22}
            # Response will be: {"name": ["Car name must contains minimum 3 symbols"]}
            raise serializers.ValidationError('Car name must contains minimum 3 symbols')
        return name

    # ВНИМАНИЕ! Название данного сериализатора зарезервированно
    def validate(self, attrs):  # attrs - это словарь, где хранятся все значения, которые прилетят с фронтенда
        """
        Данный сериализатор используется для тех случаев, когда одно значение зависит от другого.
        """
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Password mismatch!')
        return attrs
    # POST http://localhost:4000/api/v1/cars/
    # with body: {"name": "Audi", "amount":  4, "password": "qwert", "password_confirm": "qwerty"}
    # Response will be: {"non_field_errors": ["Password mismatch!"]}


# =========================================================================================
# =========================================================================================
# ============================== А У Т Е Н Т И Ф К А Ц И Я ================================
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            car = authenticate(
                username=username, password=password, request=self.context.get('request')
            )
            if not car:
                msg = 'Неверно указан username или пароль!'
                raise serializers.ValidationError(msg)

        else:
            raise serializers.ValidationError('username и пароль обязательны!')
        attrs['car'] = car
        return attrs
