from rest_framework import serializers
from .models import Quotation, QuotationItem

class QuotationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationItem
        fields = ['particular', 'ft', 'rate', 'amount']

class QuotationSerializer(serializers.ModelSerializer):
    items = QuotationItemSerializer(many=True)

    class Meta:
        model = Quotation
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        quotation = Quotation.objects.create(**validated_data)
        for item_data in items_data:
            # Create QuotationItem instances with the correct quotation reference
            QuotationItem.objects.create(quotation=quotation, **item_data)
        return quotation

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', [])

        # Update the Quotation instance
        instance = super().update(instance, validated_data)

        # Delete existing items
        QuotationItem.objects.filter(quotation=instance).delete()

        # Create new items
        for item_data in items_data:
            QuotationItem.objects.create(quotation=instance, **item_data)

        return instance



