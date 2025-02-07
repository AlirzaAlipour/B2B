from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import TopUpRequest
from .serializers import TopUpRequestSerializer
from django.db import transaction
from django.core.exceptions import ValidationError




class TopUpCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TopUpRequest.objects.all()
    serializer_class = TopUpRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        merchant = request.user.merchant
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
            






        
        

        


        