from django.db import models
from api.models.base import BaseModel
from account.models import UserAccount

class InventoryModel(BaseModel):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(UserAccount, through="UsersInventory")

    class Meta:
        db_table = "inventory"


class UsersInventory(BaseModel):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    inventory = models.ForeignKey(InventoryModel, on_delete=models.CASCADE)
    inventory_owner = models.BooleanField(default=False)

    class Meta:
        db_table = "users_inventory"


class InventoryItemsModel(BaseModel):
    name = models.CharField(max_length=255)
    qty = models.IntegerField()
    expiration_date = models.DateField()
    inventory = models.ForeignKey(InventoryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "inventory_items"