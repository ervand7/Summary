from rest_framework import serializers

from app.models import ProductCollections


class ProductCollectionsSerializer(serializers.ModelSerializer):
    """Serializer для Подборки."""

    class Meta:
        model = ProductCollections
        fields = '__all__'
