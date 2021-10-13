from rest_framework import serializers

from app.models import OrderPositions


class OrderPositionsSerializer(serializers.ModelSerializer):
    """
    Serializer для вспомогательной таблицы OrderPositions.
    """

    class Meta:
        model = OrderPositions
        fields = ["product", "quantity"]
