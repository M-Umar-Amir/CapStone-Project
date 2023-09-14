from django.contrib import admin
from .models import menu, booking
from rest_framework import authtoken
# Register your models here.
admin.site.register(menu)

admin.site.register(booking)
