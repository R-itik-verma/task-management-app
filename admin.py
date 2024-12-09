from django.contrib import admin
from .models import Task, GoogleOAuthKey

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')

@admin.register(GoogleOAuthKey)
class GoogleOAuthKeyAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'client_secret')
