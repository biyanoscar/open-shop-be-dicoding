from django.db import models

# Create your models here.
import uuid
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.TextField()
    sku = models.CharField(max_length=30)
    description = models.TextField()
    shop = models.TextField()
    location = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.CharField(max_length=30)
    stock = models.IntegerField()
    is_available = models.BooleanField()
    picture = models.TextField()
    is_delete = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
