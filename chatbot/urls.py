from django.urls import path
from . import views


urlpatterns = [
    path('chatbot/home/', views.home, name='home'),
    path('', views.chatbot, name='chatbot'),
]