from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from .models import IncreaseCreditRequest
from .serializers import IncreaseCreditRequestSerializer, UpdateCreditRequestSerializer
from django.db import transaction
from django.shortcuts import get_object_or_404




class MerchantCreditRequestView(ListCreateAPIView): #for Merchants
    permission_classes = [IsAuthenticated]
    queryset = IncreaseCreditRequest.objects.all()
    serializer_class = IncreaseCreditRequestSerializer

    def get(self, request, *args, **kwargs):
        creditreques = IncreaseCreditRequest.objects.filter(merchant = request.user.merchant)
        serializer = self.get_serializer(creditreques, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        serializer = IncreaseCreditRequestSerializer(data = request.data)
        serializer.is_valid()
        serializer.validated_data['merchant'] = request.user.merchant
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        



class CreditRequestListView(ListAPIView):    #for Admins
    permission_classes = [IsAdminUser]
    queryset = IncreaseCreditRequest.objects.filter(status ='pending')
    serializer_class = UpdateCreditRequestSerializer




class CreditRequestDetailView(RetrieveUpdateAPIView):   #for Admins
    permission_classes = [IsAdminUser]
    queryset = IncreaseCreditRequest.objects.filter(status ='pending')
    serializer_class = UpdateCreditRequestSerializer
    http_method_names = ['patch','get']

    @transaction.atomic
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        status_update = request.data.get('status')
        amount = instance.amount
        merchant = instance.merchant
        merchant.current_balance += amount
        merchant.save()
        instance.status = status_update
        instance.save()

        return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)