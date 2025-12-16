from django.db import models
class Coupon(models.Model):
    code=models.charField(max_length=50,unique=true)
