from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quotation
from .serializers import QuotationSerializer

class GenerateQuotationPDFView(APIView):

    def post(self, request):
        serializer = QuotationSerializer(data=request.data)
        if serializer.is_valid():
            quotation = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk is not None:
            return self.retrieve(request, pk)
        quotations = Quotation.objects.all().order_by("-id")
        serializer = QuotationSerializer(quotations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        try:
            quotation = Quotation.objects.get(pk=pk)
        except Quotation.DoesNotExist:
            return Response({'error': 'Quotation not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuotationSerializer(quotation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            quotation = Quotation.objects.get(pk=pk)
        except Quotation.DoesNotExist:
            return Response({'error': 'Quotation not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuotationSerializer(quotation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            quotation = Quotation.objects.get(pk=pk)
        except Quotation.DoesNotExist:
            return Response({'error': 'Quotation not found'}, status=status.HTTP_404_NOT_FOUND)

        quotation.delete()
        return Response({'message': 'Quotation deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
