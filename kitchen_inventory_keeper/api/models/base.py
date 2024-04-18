from django.db import models


class BaseModel(models.Model):
    """Model that provides a common set of attributes and operations"""
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True