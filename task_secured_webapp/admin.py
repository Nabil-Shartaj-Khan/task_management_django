from django.contrib import admin
from .models import TaskCategory, ActualTask

# Register your models here.

@admin.register(TaskCategory)
class TaskCategoryAdminSection(admin.ModelAdmin):
    fields_display = ('cat_name', 'cat_description')

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(ActualTask)
class ActualTaskAdminSection(admin.ModelAdmin):
    list_display = ('task_title', 'task_category', 'task_status', 
                    'task_priority', 'task_due_date')

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
