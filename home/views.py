from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import Item
from products.serializers import ItemSerializer


class MenuItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
class FeaturedMenuItemListView(ListAPIView):
    serializer_class=ItemSerializer
    def get_queryset(self):
        return Item.objects.filter(is_featured=True)