from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import TopUpRequest
from merchants.models import MerchantAPIKey, Merchant
from .serializers import TopUpRequestSerializer
from django.db import transaction
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from .permissions import HasMerchantAPIKey
from django.db.models import F





class TopUpCreateView(CreateAPIView):
    permission_classes = [HasMerchantAPIKey]
    queryset = TopUpRequest.objects.all()
    serializer_class = TopUpRequestSerializer

    def create(self, request, *args, **kwargs):

        
        str_api_key = request.META['HTTP_AUTHORIZATION'] 
        prefix = str_api_key.split(' ')[1].split('.')[0]
        api_key_object = get_object_or_404(MerchantAPIKey, prefix = prefix)
        serializer = self.get_serializer(data=request.data)

        # Lock the merchant row for update
        with transaction.atomic():
            merchant = Merchant.objects.get(pk=api_key_object.merchant.pk)
            
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['merchant'] = merchant

            amount = serializer.validated_data['amount']
            if amount > merchant.balance:
                return Response("Not enough credits.", status=status.HTTP_400_BAD_REQUEST)

            print(merchant.balance)
            # Update the balance using F expression
            merchant.balance  -= amount
            merchant.save(update_fields=['balance'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)







        