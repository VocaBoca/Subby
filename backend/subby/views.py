from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Subscription
from .serializers import SubscriptionSerializer
from django.db.models import Sum
from .services import monthly_avg


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        
        serializer = self.get_serializer(queryset, many=True)

        amount = queryset.count()
        total = queryset.aggregate(total=Sum("price"))["total"]

        average = monthly_avg(queryset)
        
        return Response({
            "montly_avg":average,
            "total":total,
            "amount":amount,
            "subscriptions":serializer.data
        })