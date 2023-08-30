# loan_app/urls.py
from django.urls import path
from .views import BusinessListCreateView, BalanceSheetListCreateView, SubmitApplicationView, FetchBalanceSheetView

urlpatterns = [
    path('business/', BusinessListCreateView.as_view(), name='business-list-create'),
    path('balance-sheet/', BalanceSheetListCreateView.as_view(), name='balance-sheet-list-create'),
    path('submit-application/', SubmitApplicationView.as_view(), name='submit-application'),
    path('fetch-balance-sheet/', FetchBalanceSheetView.as_view(), name='fetch-balance-sheet'),
]
