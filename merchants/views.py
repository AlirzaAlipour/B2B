from rest_framework.generics import RetrieveUpdateAPIView
from .models import Merchant
from .serializers import MerchantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
    



class MerchantProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Merchant, user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
