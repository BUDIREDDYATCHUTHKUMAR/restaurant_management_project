from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import Item
from products.serializers import ItemSerializer


class MenuItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
