from django.urls import path
from .views import MenuItemListView

urlpatterns = [
    path('menu-items/',MenuItemListView.as_view(),name='menu-item-list'),
    
]