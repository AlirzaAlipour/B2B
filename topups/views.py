from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import TopUpRequest
from merchants.models import MerchantAPIKey
from .serializers import TopUpRequestSerializer
from django.db import transaction
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from .permissions import HasMerchantAPIKey





class TopUpCreateView(CreateAPIView):
    permission_classes = [HasMerchantAPIKey]
    queryset = TopUpRequest.objects.all()
    serializer_class = TopUpRequestSerializer

    def create(self, request, *args, **kwargs):
        str_api_key = request.META['HTTP_AUTHORIZATION'] 
        prefix = str_api_key.split(' ')[1].split('.')[0]
        api_key_object = get_object_or_404(MerchantAPIKey, prefix = prefix)
        serializer = self.get_serializer(data=request.data)
        merchant = api_key_object.merchant
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['merchant'] = merchant

        with transaction.atomic():
            amount = serializer.validated_data['amount']
            if amount > merchant.current_balance:
                raise ValidationError("Not enough credits.")

            merchant.current_balance -= amount
            merchant.save() 
            serializer.save()
            return Response(serializer.data)
            







        