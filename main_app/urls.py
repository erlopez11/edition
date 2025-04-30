from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signin/', views.SignIn.as_view(), name='signin'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('editions/', views.EditionsList.as_view(), name='editions_index'),
    path('editions/<int:pk>/', views.EditionDetail.as_view(), name='edition_detail'),
    path('editions/create/', views.EditionCreate.as_view(), name='edition_create'),
    path('editions/<int:pk>/update/', views.EditionUpdate.as_view(), name='edition_update'),
    path('editions/<int:pk>/delete/', views.EditionDelete.as_view(), name='edition_delete'),
    path('editions/<int:edition_id>/add_note/', views.NoteCreate.as_view(), name='note_create'),
    path('editions/<int:edition_id>/delete_note/<int:pk>/', views.NoteDelete.as_view(), name='note_delete'),
    path('editions/<int:edition_id>/update_note/<int:pk>/', views.NoteUpdate.as_view(), name='note_update'),
    path('inks/', views.InkList.as_view(), name='inks_index'),
    path('inks/create/', views.InkCreate.as_view(), name='ink_create'),
]

