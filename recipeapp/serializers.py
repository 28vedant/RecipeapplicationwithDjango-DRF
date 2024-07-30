from rest_framework import serializers
from recipeapp.models import Recipe

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    recipe_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Recipe
        fields = ('recipe_id', 'name','ingredients','instructions','category')
