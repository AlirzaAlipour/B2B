from rest_framework.serializers import ModelSerializer
from .models import IncreaseCreditRequest


class IncreaseCreditRequestSerializer (ModelSerializer):
    class Meta:
        model = IncreaseCreditRequest
        fields = ['Salesman', 'request_amount', 'requested_at', 'status']
        read_only_fields = ['status']