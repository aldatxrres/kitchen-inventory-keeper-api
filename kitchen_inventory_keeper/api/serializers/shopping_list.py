from rest_framework import serializers
from api.models.shopping_list import ShoppingListModel, ShoppingListItemsModel


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ShoppingListModel
    

class ShoppingListItemsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ShoppingListItemsModel