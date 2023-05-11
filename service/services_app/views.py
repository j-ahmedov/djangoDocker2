from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from services_app.models import Subscription
from services_app.serializers import SubscriptionSerializer


# Create your views here.
class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
