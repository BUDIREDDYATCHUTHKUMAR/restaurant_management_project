from rest_framework import serializers
from .models import Order,OrderItem,OrderStatus,Coupon
from products.serializers import ItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    item=ItemSerializer(read_only=True)
    class Meta:
        model=OrderItem
        fields=['item','quantity','price']
class OrderHistorySerializer(serializer.ModelSerializer):
    items=OrderItemserializer(source='order_items',many=True,),read_only=True)
    class Meta:
        model=Order
        fields=['id','created_at','total_price','status','items']
class OrderSerializer(serializer.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coupon
        fields='__all__'