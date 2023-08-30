from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from loan_app.models import Business, BalanceSheet
from loan_app.serializers import BusinessSerializer, BalanceSheetSerializer
from loan_app.logic import calculate_pre_assessment


class FetchBalanceSheetView(APIView):
    def post(self, request, *args, **kwargs):
        selected_business_id = request.data.get('business_id')  # Get selected business ID from request
        print("********",selected_business_id)
        # Fetch balance sheet data from accounting software provider
        # Logic to fetch data goes here
        fetched_data = [
            
        ]  # Replace with fetched data from accounting software

        # Create balance sheet entries based on fetched data
        for entry_data in fetched_data:
            serializer = BalanceSheetSerializer(data={**entry_data, 'business': selected_business_id})
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Balance sheet data imported successfully."}, status=status.HTTP_200_OK)