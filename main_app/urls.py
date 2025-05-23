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
    path('inks/delete_ink/<int:pk>/', views.InkDelete.as_view(), name='ink_delete'),
    path('inks/update_ink/<int:pk>/', views.InkUpdate.as_view(), name='ink_update'),
    path('editions/<int:edition_id>/associate_ink/<int:ink_id>/', views.associate_ink, name='associate_ink'),
    path('editions/<int:edition_id>/remove_ink/<int:ink_id>/', views.remove_ink, name='remove_ink'),
    path('papers/', views.PaperList.as_view(), name='paper_index'),
    path('papers/create/', views.PaperCreate.as_view(), name='paper_create'),
    path('papers/delete_paper/<int:pk>/', views.PaperDelete.as_view(), name='paper_delete'),
    path('papers/update_paper/<int:pk>/', views.PaperUpdate.as_view(), name='paper_update'),
    path('editions/<int:edition_id>/associate_paper/<int:paper_id>/', views.associate_paper, name='associate_paper'),
    path('editions/<int:edition_id>/remove_paper/<int:paper_id>/', views.remove_paper, name='remove_paper'),
    path('archive/', views.archive_list, name='archive_list'),
]

