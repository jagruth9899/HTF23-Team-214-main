# myapp/urls.py
from django.urls import path
from login import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
     path('home/', views.home_view, name='home')
]
