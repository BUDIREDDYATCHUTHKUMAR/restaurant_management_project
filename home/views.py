from django.shortcuts import render
from rest_framework.generic import ListAPIView
from products.models import Item
from products.serializers import ItemSerializer

# Create your views here.
class MenuItemSerializer(ListAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
