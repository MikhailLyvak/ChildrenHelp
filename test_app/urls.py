from django.urls import path
from .views import register, login_view, profile_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile_view/', profile_view, name='profile_view'),
]

app_name = 'test_app'