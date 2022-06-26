from django.urls import path, include
from .views import lottoAPI

urlpatterns = [
    path('num/', lottoAPI),
]