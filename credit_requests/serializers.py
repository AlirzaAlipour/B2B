from rest_framework.serializers import ModelSerializer
from .models import IncreaseCreditRequest


class IncreaseCreditRequestSerializer (ModelSerializer):
    class Meta:
        model = IncreaseCreditRequest
        fields = ['id', 'merchant', 'request_amount', 'requested_at', 'status']
        read_only_fields = ['id', 'status', 'merchant']




class UpdateCreditRequestSerializer (ModelSerializer):
    class Meta:
        model = IncreaseCreditRequest
        fields = ['id', 'merchant', 'request_amount', 'requested_at', 'status']
        read_only_fields = ['id', 'merchant', 'request_amount', 'requested_at']