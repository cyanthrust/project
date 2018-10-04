from django.contrib import admin
from .models import Character, active_Character

# Register your models here.
admin.site.register(Character)
admin.site.register(active_Character)