from django.urls import path
from . import views

app_name = "blog"  # define application namespace
# domain.com/blog/...
urlpatterns = [
    path('anouncement_detail/<slug:slug>/<int:id>/', views.get_announcement, name='anouncement_detail'),
    path("", views.announcement_list, name="announcement_list"),
]
