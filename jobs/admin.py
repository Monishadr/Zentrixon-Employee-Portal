from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'job_title')
