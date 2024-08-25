from django.db import models

class Quotation(models.Model):
    client_name = models.CharField(max_length=255)
    client_address = models.CharField(max_length=255)
    quotation_date = models.DateField()
    gst_percentage = models.FloatField()

class QuotationItem(models.Model):
    quotation = models.ForeignKey(Quotation, related_name='items', on_delete=models.CASCADE)
    particular = models.CharField(max_length=255)
    ft = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
