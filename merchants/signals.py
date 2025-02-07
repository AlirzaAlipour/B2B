from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Merchant



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def handle_merchant_profile(sender, instance, created, **kwargs):

    if created:
        if not instance.is_staff:
            Merchant.objects.create(user=instance)
    else:
        if hasattr(instance, 'merchant') and not instance.is_staff:
            instance.merchant.save()