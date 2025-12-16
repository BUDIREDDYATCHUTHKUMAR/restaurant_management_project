# orders/views.py
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Coupon


class CouponValidationView(APIView):
    def post(self, request, *args, **kwargs):
        code = request.data.get("code")
        if not code:
            return Response(
                {"success": False, "error": "Coupon code is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        now = timezone.now()
        try:
            coupon = Coupon.objects.get(
                code=code,
                is_active=True,
                valid_from__lte=now,
                valid_to__gte=now,
            )
        except Coupon.DoesNotExist:
            return Response(
                {"success": False, "error": "Invalid or expired coupon."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "success": True,
                "code": coupon.code,
                "discount_percentage": float(coupon.discount_percentage),
            },
            status=status.HTTP_200_OK,
        )
