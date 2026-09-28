from django.db import models
from core.models import PublishedModel, CreatedModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(PublishedModel, CreatedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)

class Location(PublishedModel, CreatedModel):
    name = models.CharField(max_length=256)

class Post(PublishedModel, CreatedModel):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=CASCADE)
    location = models.ForeignKey(Location, on_delete=SET_NULL,
                                 null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL,
                                 null=True)
