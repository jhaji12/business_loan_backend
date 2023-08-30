from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from loan_app.models import Business, BalanceSheet
from loan_app.serializers import BusinessSerializer, BalanceSheetSerializer
from loan_app.logic import calculate_pre_assessment

class SubmitApplicationView(APIView):
    def post(self, request, *args, **kwargs):
        # Assuming request contains necessary data for application
        
        balance_sheet_data = request.data.get('balanceSheetData', {})
        business = request.data.get('business', {})
        print("######")
        print(business)

        # Calculate pre-assessment using the provided logic
        pre_assessment = calculate_pre_assessment(business=business, balanceSheetData=balance_sheet_data)

        # Submit application data to decision engine
        # Logic to interact with decision engine goes here
        decision_outcome = "approved" if pre_assessment >= 60 else "rejected"

        # Return decision outcome and pre-assessment value to frontend
        return Response({"decision": decision_outcome, "pre_assessment": pre_assessment}, status=status.HTTP_200_OK)
