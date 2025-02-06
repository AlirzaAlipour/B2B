from django.db import models
from accounts.models import Merchant

class TopUpRequest(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='topup_requests')
    phone_number = models.TextField()
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


