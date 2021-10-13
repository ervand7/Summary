from collections import defaultdict

from rest_framework import serializers

from app.models import Product, Order, OrderPositions
from .order_positions_serializer import OrderPositionsSerializer


class OrderSerializer(serializers.ModelSerializer):
    """Serializer для Заказа."""
    # тут мы только для сериализации создаем поле positions в классе Order, которое будет
    # просериализованно уже через свой собственный сериализатор OrderPositionsSerializer.
    # В БД это поле представляется таблицей от класса OrderPositions
    positions = OrderPositionsSerializer(many=True)

    class Meta:
        model = Order
        fields = "id", "status", "total_sum", "created_at", "updated_at", "positions"

    @staticmethod
    def get_product_list(positions):
        """
        Собирает в список продукты, каждый из которых представлен в виде
        инстанса класса Product.
        """
        product_list = []
        for position in positions:
            product_queryset = Product.objects.filter(id=position['product'])
            product_list.append(list(product_queryset)[0])
        return product_list

    @staticmethod
    def calculate_total_sum(positions):
        """
        Высчитывает total_sum заказа.
        """
        order_total_sum = 0
        for pos in positions:
            product_id = pos['product']
            product_quantity = pos['quantity']
            product_queryset = Product.objects.filter(id=product_id)
            product_price = list(product_queryset.values_list('price', flat=True))[0]
            product_sum = product_price * product_quantity
            order_total_sum += product_sum
        return order_total_sum

    @staticmethod
    def fill_OrderPositions(positions, order, product_list):
        """
        Заполняет поля класса OrderPositions ранее подготовленными значениями.
        """
        for product_index in range(len(positions)):
            OrderPositions.objects.create(
                order=order,
                product=product_list[product_index],
                quantity=positions[product_index]["quantity"]
            )

    @staticmethod
    def check_duplicate_positions(attrs):
        """
        Функция возбуждает исключение, если пользователь в positions прописал товар более одного раза.
        Не путать с кол-вом товара. У одного товара может быть неограниченное его кол-во в заказе,
        однако поле {товар: его_кол-во} должно быть уникальным.
        """
        failed_msg = 'This products were passed more them one time: %s'
        positions_counter = defaultdict(lambda: 0)
        products_ids = [position['product'].id for position in attrs['positions']]
        for product_id in products_ids:
            positions_counter[product_id] += 1
        duplicated_positions = list(
            {key: value for key, value in positions_counter.items() if value > 1}.keys()
        )
        if duplicated_positions:
            raise serializers.ValidationError(failed_msg % duplicated_positions)

    def validate(self, attrs):
        """
        Эта заоверрайденная функция вызывается перед create и update.
        Тут мы валидируем некоторые входные параметры в соответствии с нашими требованиями.
        """
        # чтобы пользователь в positions не мог 2 раза прописать один и тот же товар
        self.check_duplicate_positions(attrs)
        # чтобы записывалась информация о позициях заказа
        attrs['positions'] = self.initial_data.get('positions')
        # чтобы калькулировался и записывался total_sum
        positions = attrs['positions']
        attrs['total_sum'] = self.calculate_total_sum(positions)

        # валидируем отправку несуществующих продуктов
        order_products_ids = [pos['product'] for pos in positions]
        all_products_ids = list(Product.objects.values_list('id', flat=True))
        if set(order_products_ids) | set(all_products_ids) != set(all_products_ids):
            raise serializers.ValidationError('Non exist products were passed!')
        return attrs

    def create(self, validated_data):
        """
        Отверрайдим родительский метод для того, чтобы можно было:
        1) сериализовать поле positions (представляет собой доп. таблицу)
        2) калькулировать total_sum
        """
        # чтобы записывалась информация о текущем отправителе запроса
        validated_data['user'] = self.context['request'].user
        # удаляем positions из validated_data так как это поле создадим через класс
        # OrderPositions. А удаленное через pop значение используем для получения различных данных
        positions = validated_data.pop("positions")
        # и создаем заказ
        order = super().create(validated_data)

        # сериализуем поле positions для нашего Order
        # сначала набираем в product_list инстансы от класса Product
        product_list = self.get_product_list(positions)
        # затем заполняем поле positions у класса Order через заполнение класса OrderPositions
        self.fill_OrderPositions(positions, order, product_list)
        return order

    def update(self, instance, validated_data):
        """
        Отверрайдим родительский метод для того, чтобы можно было:
        1) сериализовать поле positions при update и partial update
        2) калькулировать total_sum при update и partial update
        """
        positions = validated_data.pop("positions")
        if positions:
            validated_data["total_sum"] = self.calculate_total_sum(positions)
            # обновляем заказ через родительский метод
            update_order = super().update(instance, validated_data)
            # очищаем positions
            update_order.positions.all().delete()
            # заполняем positions
            product_list = self.get_product_list(positions)
            self.fill_OrderPositions(positions, update_order, product_list)
            return update_order
