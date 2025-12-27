from django.utils.crypto import get_random_string
from .models import Coupon
def generate_coupon_code(length=10):
    while True:
        code=get_random_string(length=length)
        if not Coupon.objects.filter(code==code).exists():
            return code