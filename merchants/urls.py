from django.urls import path
from .views import MerchantProfileView, MerchantAPIKeyView
from credit_requests.views import MerchantCreditRequestView

urlpatterns = [
    path("", MerchantProfileView.as_view()),
    path("credit-requests/", MerchantCreditRequestView.as_view()),
    path("api-key", MerchantAPIKeyView.as_view())
]
