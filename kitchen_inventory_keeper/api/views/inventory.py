from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction
from datetime import datetime

from api.models.inventory import InventoryModel, UsersInventory, InventoryItemsModel
from api.serializers.inventory import InventorySerializer, InventoryItemsSerializer, ExpiredItemsSerializer
from api.pagination import CustomLimitOffsetPagination

class InventoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = InventorySerializer
    
    def get_queryset(self):
        if self.request.user.is_anonymous:
            return InventoryModel.objects.all()
        
        return InventoryModel.objects.filter(users=self.request.user)

    def perform_create(self, serializer):
        with transaction.atomic():
            inventory = serializer.save()

            UsersInventory.objects.create(user=self.request.user, inventory=inventory, inventory_owner=True)
            


class InventoryItemsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = InventoryItemsSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['inventory']

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return InventoryItemsModel.objects.all()

        return InventoryItemsModel.objects.filter(inventory__users=self.request.user)


    @action(methods=["GET"], detail=False)
    def get_expired_items(self, request):
        queryset = self.get_queryset().filter(expiration_date__lte=datetime.now().date())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ExpiredItemsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ExpiredItemsSerializer(queryset, many=True)
        return Response(serializer.data)