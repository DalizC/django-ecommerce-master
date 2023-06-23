from rest_framework import serializers
from .models import Item, OrderItem, Order


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'price')
