from django.contrib import admin
from django.urls import path, include
from accounts.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home-view'),
    path('', include('chatbot.urls')),
    path('', include('accounts.urls')),
]
