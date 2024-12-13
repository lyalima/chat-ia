from django.urls import path
from .views import RegisterView, LoginView, LogoutView


urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login-view'),
    path('accounts/register/', RegisterView.as_view(), name='register-view'),
    path('accounts/logout/', LogoutView.as_view(), name='logout-view'),
]
