from django.apps import AppConfig


class MerchantsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "merchants"

    def ready(self):
        import merchants.signals
