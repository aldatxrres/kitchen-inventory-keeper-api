from django.db import models
from api.models.base import BaseModel
from account.models import UserAccount

class RecipeModel(BaseModel):
    title = models.CharField(max_length=150)
    ingredients = models.TextField()
    method = models.TextField()
    total_time = models.IntegerField()
    observations = models.TextField()
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    class Meta:
        db_table = "recipe"