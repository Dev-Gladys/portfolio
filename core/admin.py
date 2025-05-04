from django.contrib import admin
from .models import GladysOro,Project,Message

@admin.register(GladysOro)
class GladysOroAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'location', 'email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')