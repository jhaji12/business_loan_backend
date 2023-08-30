from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from loan_app.models import BalanceSheet
from loan_app.serializers import BalanceSheetSerializer


class BalanceSheetListCreateView(generics.ListCreateAPIView):
    serializer_class = BalanceSheetSerializer
    # Call the API of Accounting software to fetch balance sheet for a selected business of the user
    
    def get_queryset(self):
        business_id = self.request.query_params.get("business_id")

        queryset = BalanceSheet.objects.all()

        if business_id:
            queryset = queryset.filter(business_id=business_id)

        return queryset
