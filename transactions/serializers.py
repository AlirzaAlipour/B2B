from rest_framework.serializers import ModelSerializer
from .models import TopUpRequest

class TopUpRequestSerializer(ModelSerializer):
    class Meta:
        model = TopUpRequest
        fields = ['merchant', 'phone_number', 'amount']