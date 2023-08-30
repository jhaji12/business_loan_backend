from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from loan_app.models import Business
from loan_app.serializers import BusinessSerializer

class BusinessListCreateView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

