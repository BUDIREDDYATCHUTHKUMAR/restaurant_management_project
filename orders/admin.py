from django.contrib import admin
from .models import Order,OrderItem,OrderStatus,Coupon

@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display=['code','discount_percentage','is_active','valid_from','valid_to']
    list_filter=['is_active']
class OrderItemInline(admin.TabularInline):
    model=OrderItem
    extra=1
@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','customer_name','total_price','status','cretaed_at']
    list_filter=['status','created_at']
    inlines=[OrderItemInline]
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order','item','quantity','price']

# Register your models here.
