from .models import Merchant, MerchantAPIKey
from rest_framework.serializers import ModelSerializer




class MerchantSerializer (ModelSerializer):
    class Meta:
        model = Merchant 
        fields = ['user', 'company_name', 'current_balance']
        read_only_fields = ['user','current_balance']


class MerchantAPIKeySerializer(ModelSerializer):
    class Meta:
        model = MerchantAPIKey  # Ensure this points to your correct API key model
        fields = ['id', 'prefix', 'hashed_key', 'created', 'revoked', 'expiry_date', 'merchant', 'name']
        read_only_fields = ['merchant']
