from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    inventory,
)

router = DefaultRouter()

router.register(r"inventory", inventory.InventoryViewSet, basename="inventory")
router.register(r"inventory_items", inventory.InventoryItemsViewSet, basename="inventory_items")


urlpatterns = [
    path("", include(router.urls)),
]