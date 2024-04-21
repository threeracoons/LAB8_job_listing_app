from django.contrib import admin

# Register your models here.
# JOBS/admin.py
from django.contrib import admin
from .models import Job

admin.site.register(Job)
