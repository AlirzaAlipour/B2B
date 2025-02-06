from .models import Merchant
from rest_framework.serializers import ModelSerializer




class MerchantSerializer (ModelSerializer):
    class Meta:
        model = Merchant 
        fields = ['user', 'company_name', 'current_balance']
