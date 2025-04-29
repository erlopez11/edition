from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signin/', views.SignIn.as_view(), name='signin'),
    path('accounts/signup/', views.signup, name='signup'),
]

