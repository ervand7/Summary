from rest_framework import serializers
from .models import Car


# ============================== БАЗОВЫЙ СЕРИАЛИЗАТОР (Serializer)=================================
# Воспользуемся джанговским БАЗОВЫМ сериализатором для сериализации и десериализации.
# Для этого мы создадим собственный класс, наследуемый от rest_framework.serializers.Serializer
class CarSerializer(serializers.Serializer):
    # тут мы прописываем поля из модели Car и задаем им настройки преобразований
    id = serializers.IntegerField(read_only=True)  # read_only=True означает, что мы это поле не трогаем
    name = serializers.CharField()


# ========================= ПРОДВИНУТЫЙ СЕРИАЛИЗАТОР (ModelSerializer) =============================
# Воспользуемся джанговским ПРОДВИНУТЫМ сериализатором, чтобы из модели сформировать сериализованный объект
class CarSerializerFromModelSerializer(serializers.ModelSerializer):
    """
    ModelSerializer самостоятельно выводит типы на основании указанной в Meta модели.
    """
    class Meta:
        # заполняем обязательные 2 поля: model и fields
        model = Car  # прописываем название модели
        # прописываем поля, которые нас интересуют
        fields = '__all__'  # можно также прописать кортежем: ('id', 'name')
