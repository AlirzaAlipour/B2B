from rest_framework.generics import RetrieveUpdateAPIView, GenericAPIView
from .models import Merchant, MerchantAPIKey
from .serializers import MerchantSerializer, MerchantAPIKeySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from topups.serializers import TopUpRequestSerializer
from rest_framework.views import APIView

    



class MerchantProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Merchant, user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

        

class MerchantAPIKeyView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MerchantAPIKey.objects.all()
    serializer_class = MerchantAPIKeySerializer

    def post(self, request, *args, **kwargs):
        # Generate a new API key for the authenticated merchant
        merchant = request.user.merchant
        name = f"{merchant.company_name} Key"
        
        # Delete existing API keys before creating a new one
        merchant.apikey.all().delete()
        
        # Create a new API key
        api_key_instance, generated_key = MerchantAPIKey.objects.create_key(name=name, merchant=merchant)
        response_data = self.get_serializer(api_key_instance).data
        response_data['api_key'] = generated_key
        response_data['warning'] = "SECURELY STORE THIS KEY - IT WON'T BE SHOWN AGAIN"
        
        return Response(response_data, status=status.HTTP_201_CREATED)

    