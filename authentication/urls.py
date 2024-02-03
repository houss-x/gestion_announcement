from django.urls import path
from . import views
app_name = 'authentication'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('portail/', views.user_list, name='adminportail'),
    path('toggle_user_status/<int:user_id>/', views.toggle_user_status, name='statusswitch'),

]