from django.urls import path
from rest_framework import routers
from .views import TaskViewSet, RegisterView

routers = routers.DefaultRouter()
routers.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]

urlpatterns += routers.urls