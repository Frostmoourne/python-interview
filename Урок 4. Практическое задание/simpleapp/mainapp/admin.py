from django.contrib import admin
from django.contrib.admin import site

from .models import Items

# Register your models here.

admin.site.register(Items)
