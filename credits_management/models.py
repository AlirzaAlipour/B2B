from django.db import models
from accounts.models import Merchant


class IncreaseCreditRequest (models.Model):
    REQUEST_STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='credit_requests')
    request_amount = models.PositiveIntegerField()
    requested_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=REQUEST_STATUS, default='pending')