from django.contrib import admin
from recipeapp.models import Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display=['recipe_id', 'name','ingredients','instructions','category']


admin.site.register(Recipe,RecipeAdmin)
