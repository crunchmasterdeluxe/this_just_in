from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Headline(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    headline = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse(
            "game:headlines",
            kwargs = {
                "pk": self.pk,
                "category": self.category.pk
            }
        )

class Intro(models.Model):
    intro = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.intro
    