from rest_framework import serializers
from item.models import Category as CategoryModel
from item.models import Item as ItemModel
from item.models import Order as OrderModel
from item.models import ItemOrder as ItemOrderModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        feilds = ['name']


class OrderSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    def get_item(self, obj):
        return obj.item.name

    class Meta:
        model = OrderModel
        feilds = ['delivery_address', 'order_date', 'item', ]


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrderModel
        feilds = ['order', 'item', 'item_count', ]


class ItemSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()

    class Meta:
        model = ItemModel
        feilds = ['__all__']