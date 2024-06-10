from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    inventory,
    shopping_list,
    recipe
)

router = DefaultRouter()

router.register(r"inventory", inventory.InventoryViewSet, basename="inventory")
router.register(r"inventory_items", inventory.InventoryItemsViewSet, basename="inventory_items")
router.register(r"shopping_list", shopping_list.ShoppingListViewSet, basename="shopping_list")
router.register(r"shopping_list_items", shopping_list.ShoppingListItemsViewSet, basename="shopping_list_items")
router.register(r"recipe", recipe.RecipeViewSet, basename="recipe")

urlpatterns = [
    path("", include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]