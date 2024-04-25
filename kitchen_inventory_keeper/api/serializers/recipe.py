from rest_framework import serializers
from api.models.recipe import RecipeModel

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeModel
        exclude = ('user',)