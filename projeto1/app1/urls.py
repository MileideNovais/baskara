from django.urls import path
from . views import baskara_view

urlpatterns = [
    path('', baskara_view),
]