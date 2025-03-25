from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_task, name='task_list'),
    path('task/<int:task_id>/', views.specific_task_detail, name='task_detail'),
    path('task/create/', views.task_creation, name='task_create'),
    path('categories/', views.task_category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_based_tasks, name='category_tasks'),
]
