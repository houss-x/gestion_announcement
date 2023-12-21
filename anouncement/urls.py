from django.urls import path
from . import views

app_name = 'announcement'  # Set the app_name if you are using namespaced URLs

urlpatterns = [
    path("", views.announcement_list, name='anouncement_list'),
    # Add other URL patterns for the announcement app
]