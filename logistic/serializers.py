from rest_framework import serializers
from rest_framework.parsers import JSONParser

from logistic.models import Product, Stock, StockProduct


#
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title", 'description')
#
class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ('product', 'quantity', "price")
    # настройте сериализатор для позиции продукта на складе

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ("address", 'positions')
    # настройте сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for anyposition in positions:
            StockProduct.objects.create(stock=stock, **anyposition)
        #
        return stock
    #
    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(positions)
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        #
        for element in positions:
            print(element)
            print('__________________')
            obj, created = StockProduct.objects.update_or_create(stock=stock,
                                                                 product=element['product'],
                                                                 defaults={'stock': stock,
                                                                           'product': element['product'],
                                                                           'quantity': element['quantity'],
                                                                           'price': element['price']})
        return stock
