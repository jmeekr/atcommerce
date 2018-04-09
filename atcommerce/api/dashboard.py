from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from .models import Eorders, Product, Customer
from datetime import datetime, timedelta

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eorders
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

class DashboardViewSet(viewsets.ModelViewSet):
    """
    This view should order by date the last 24 hour orders
    so long as the user has permissions to access the view

    And be able to update Transactions
    """

    # Order by the past 24 hours
    queryset = Eorders.objects.filter(order_date__gt=datetime.now() - timedelta(days=1)).order_by('-order_date')
    serializer_class = DashboardSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = DashboardSerializer(queryset, many=True)
        return Response(serializer.data)
