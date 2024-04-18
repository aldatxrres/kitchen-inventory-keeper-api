from rest_framework import serializers
from api.models.inventory import InventoryModel, InventoryItemsModel


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = InventoryModel
    

class InventoryItemsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = InventoryItemsModel