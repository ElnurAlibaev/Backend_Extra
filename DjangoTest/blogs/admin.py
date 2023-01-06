from django.contrib import admin
from . import models

# Чтобы моделька показывалась в админке 
admin.site.register(models.Blog) 
