from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signin/', views.SignIn.as_view(), name='signin'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('editions/', views.EditionsList.as_view(), name='editions_index'),
    path('editions/<int:pk>/', views.EditionDetail.as_view(), name='edition_detail'),
]

