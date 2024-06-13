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
    

class ExpiredItemsSerializer(serializers.ModelSerializer):
    inventory = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        fields = "__all__"
        model = InventoryItemsModel