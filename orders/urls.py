from django.urls import path
from .views import CouponValidationView

urlpatterns = [
    path("coupons/validate/", CouponValidationView.as_view(), name="couons_validate"),
    path("my-orders/",UserOrderHistoryView.as_view(),name='user-order-history'),
    
]
