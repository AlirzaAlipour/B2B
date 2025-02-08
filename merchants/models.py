from pyexpat import model
from django.conf import settings
from django.db import models
from rest_framework_api_key.models import AbstractAPIKey
from django.core.exceptions import ValidationError




class Merchant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='merchant')
    company_name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)

    def clean(self):
        if self.balance < 0:
            raise ValidationError('Current balance cannot be negative.')


class MerchantAPIKey(AbstractAPIKey):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='apikey')