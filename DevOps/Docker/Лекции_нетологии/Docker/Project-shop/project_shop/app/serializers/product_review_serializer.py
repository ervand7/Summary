from rest_framework import serializers

from app.models import ProductReview


class ProductReviewSerializer(serializers.ModelSerializer):
    """Serializer для Отзыва."""

    class Meta:
        model = ProductReview
        fields = '__all__'

    def validate(self, attrs):
        # чтобы автоматически записывался id создателя
        attrs["creator"] = self.context['request'].user
        return attrs

    def create(self, validated_data):
        """
        The function allows the user to leave only one review for the same product.
        """
        failed_msg = 'You have already left a review for this product!'
        request = self.context.get('request')
        creator = request.user
        product = validated_data['product']
        if ProductReview.objects.filter(creator=creator, product=product).exists():
            raise serializers.ValidationError(failed_msg)
        review = super().create(validated_data)
        return review

