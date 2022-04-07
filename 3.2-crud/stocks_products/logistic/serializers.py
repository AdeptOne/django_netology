from pprint import pprint

from django.db import models
from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        # StockProduct.objects.create(stock=stock, **positions)
        for position in positions:
            position['stock'] = stock
            position = (StockProduct(stock=position['stock'], product=position['product'],
                                     quantity=position['quantity'], price=position['price'])).save()
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        print(instance)
        stock = super().update(instance, validated_data)
        for position in positions:
            position['stock'] = stock
            position = (StockProduct(stock=position['stock'], product=position['product'],
                                     quantity=position['quantity'], price=position['price'])).save()
        return stock

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']
