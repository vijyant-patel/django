from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet)
app_name = "interview_02"

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_task, name='interview_02-add'),
    path('edit/<int:task_id>', views.edit_task, name='interview_02-edit'),
    path('delete/<int:task_id>', views.delete_task, name='interview_02-delete'),
    path('api/', include(router.urls)),

]