from django.urls import path
from . import views

app_name = 'announcement'  # Set the app_name if you are using namespaced URLs

urlpatterns = [
    path("", views.announcement_list, name='anouncement_list'),
    path("my", views.my_announcement, name='my_anouncement'),
    path('delete/<int:announcement_id>/', views.delete_announcement, name='delete_announcement'),
    path('edit/<int:pk>/', views.edit_announcement, name='edit_anouncement')
] 