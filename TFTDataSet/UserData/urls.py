from django.urls import path, include
from rest_framework.routers import DefaultRouter
from UserData import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'user', views.UsersView, basename="users")

urlpatterns = [
    path('', include(router.urls)),
]