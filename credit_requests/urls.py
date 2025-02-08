from django.urls import path
from .views import CreditRequestListView, CreditRequestDetailView

urlpatterns = [
    path("credit-requests", CreditRequestListView.as_view()),
    path("credit-requests/<int:pk>/", CreditRequestDetailView.as_view(), name='credit-requests')
]