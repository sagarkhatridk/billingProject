from django.urls import path
from .views import GenerateQuotationPDFView

urlpatterns = [
    path('quotations/', GenerateQuotationPDFView.as_view(), name='create-list-quotations'),
    path('quotations/<int:pk>/', GenerateQuotationPDFView.as_view(), name='retrieve-update-quotation'),
]
