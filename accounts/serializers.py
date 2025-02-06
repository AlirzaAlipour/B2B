from .models import SalesmanProfile, ApproverProfile
from rest_framework.serializers import ModelSerializer



class ApproverProfileSerializer (ModelSerializer):
    class Meta:
        model = ApproverProfile
        fields = ['user', 'department']



class SalesmanProfileSerializer (ModelSerializer):
    class Meta:
        model = SalesmanProfile
        fields = ['user', 'company_name', 'current_balance']
