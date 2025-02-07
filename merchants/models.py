from pyexpat import model
from django.conf import settings
from django.db import models
from rest_framework_api_key.models import AbstractAPIKey




class Merchant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='merchant')
    company_name = models.CharField(max_length=100)
    current_balance = models.PositiveIntegerField(default=0)


class MerchantAPIKey(AbstractAPIKey):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='apikey')