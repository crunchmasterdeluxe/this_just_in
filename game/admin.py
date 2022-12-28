from django.contrib import admin

# Register your models here.

from .models import Category, Headline, Intro

admin.site.register(Category)
admin.site.register(Headline)
admin.site.register(Intro)