from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, recipe_list, recipe_detail, recipe_new, recipe_edit, recipe_delete

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    # API Routes
    path('api/', include(router.urls)),
    # Template-based Routes
    path('', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipe/new/', recipe_new, name='recipe_new'),
    path('recipe/<int:pk>/edit/', recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
]
