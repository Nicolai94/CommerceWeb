from django.urls import path
from .views import *

urlpatterns = [
    path('users', UserProfileViewSet.as_view()),
]