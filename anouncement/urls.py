from django.urls import path
from . import views

app_name = "blog"  # define application namespace
# domain.com/blog/...
urlpatterns = [
    path("", views.announcement_list, name="announcement_list"),
]
