import os
from django.db import models
from django.utils.crypto import get_random_string


def create_id():
    return get_random_string(22)

def upload_image_to(instance, filename):
    item_id = instance.id
    return os.path.join('static', 'items', item_id, filename)

class Tag(models.Model):
    slug = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    slug = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    id = models.CharField(default=create_id, primary_key=True, max_length=22, 
    editable=False)
    name = models.CharField(default="", max_length=50)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(default="", blank=True)
    sold_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)
    image = models.ImageField(default="", upload_to=upload_image_to, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name