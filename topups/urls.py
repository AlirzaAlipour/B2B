from django.urls import path
from .views import TopUpCreateView

urlpatterns = [
    path("", TopUpCreateView.as_view(), name='topup')
]
