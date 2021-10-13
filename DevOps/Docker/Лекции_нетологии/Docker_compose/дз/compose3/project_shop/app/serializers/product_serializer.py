from rest_framework import serializers

from app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer для Продукта."""

    class Meta:
        model = Product
        fields = '__all__'
