from django.urls import path
from .views import MenuItemListView
from .views import FeaturedMenuItemListView

urlpatterns = [
    path('menu-items/', MenuItemListView.as_view(), name='menu-item-list'),
    path('featured-menu-items/',FeaturedMenuItemListView.as_view(),name='featured-menu-item-list'),

]
