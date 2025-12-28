from django.db import models

# Create your models here.
class Coupon(models.Model):
    code=models.CharField(max_length=50,unique=True)
    discount_percentage=models.DecimalField(max_digits=5,decimal_places=2)
    is_active=models.BooleanField(default=True)
    valid_from=models.DateTimeField()
    valid_to=models.DateTimeField()

    def __str__(self):
        return f"{self.code}({self.discount_percentage}% off)"
class OrderStatus(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
class OrderItem(models.Model):
    order=models.ForeignKey('order',on_delete=models.CASCADE,related_name='order_items')
    item=models.ForeignKey('products.Item',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=8,decimal_places=2)
class Orders(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE,default=1)
    customer_name=models.CharField(max_length=100)
    customer_email=models.EmailField()
    status=models.Foreign_Key(OrderStatus,on_delete=SET_NULL,null=True,blank=True)
    total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk}"