from django.conf import settings
from django.db import models
from rest_framework_api_key.models import AbstractAPIKey
from django.core.validators import MinValueValidator




class Merchant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='merchant')
    company_name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0, validators=[MinValueValidator(1)])


class MerchantAPIKey(AbstractAPIKey):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='apikey')