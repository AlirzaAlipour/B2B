from django.urls import path
from .views import MerchantProfileView
from credit_requests.views import MerchantCreditRequestView

urlpatterns = [
    path("", MerchantProfileView.as_view()),
    path("credit-requests/", MerchantCreditRequestView.as_view()),
    
]
