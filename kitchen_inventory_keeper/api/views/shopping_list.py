from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction

from api.models.shopping_list import ShoppingListModel, UserShoppingList, ShoppingListItemsModel
from api.serializers.shopping_list import ShoppingListSerializer, ShoppingListItemsSerializer

class ShoppingListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ShoppingListSerializer
    
    def get_queryset(self):
        if self.request.user.is_anonymous:
            return ShoppingListModel.objects.all()
        
        return ShoppingListModel.objects.filter(users=self.request.user)

    def perform_create(self, serializer):
        with transaction.atomic():
            shopping_list = serializer.save()

            UserShoppingList.objects.create(user=self.request.user, shopping_list=shopping_list, shopping_list_owner=True)
            


class ShoppingListItemsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ShoppingListItemsSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['shopping_list']

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return ShoppingListItemsModel.objects.all()

        return ShoppingListItemsModel.objects.filter(shopping_list__users=self.request.user)