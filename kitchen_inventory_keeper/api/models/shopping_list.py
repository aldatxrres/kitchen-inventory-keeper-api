from django.db import models
from api.models.base import BaseModel
from account.models import UserAccount

class ShoppingListModel(BaseModel):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(UserAccount, through="UserShoppingList")

    class Meta:
        db_table = "shopping_list"


class UserShoppingList(BaseModel):
    user = models.ForeignKey(UserAccount, on_delete=models.PROTECT)
    shopping_list = models.ForeignKey(ShoppingListModel, on_delete=models.PROTECT)
    shopping_list_owner = models.BooleanField(default=False)

    class Meta:
        db_table = "users_shopping_list"


class ShoppingListItemsModel(BaseModel):
    name = models.CharField(max_length=255)
    qty = models.IntegerField()
    purchased = models.BooleanField()
    shopping_list = models.ForeignKey(ShoppingListModel, on_delete=models.PROTECT)

    class Meta:
        db_table = "shopping_list_items"