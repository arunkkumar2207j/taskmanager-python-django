from rest_framework import routers
from .views import TaskViewSet

routers = routers.DefaultRouter()
routers.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = routers.urls