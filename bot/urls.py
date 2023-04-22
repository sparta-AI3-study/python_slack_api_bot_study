from django.urls import path
from bot import views

urlpatterns = [
    path('send', views.SendSlackAPI.as_view(), name='send'),
]