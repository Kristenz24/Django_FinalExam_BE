from django.urls import path
from . import views

urlpatterns = [
    path ('register/', views.register, name='register'),
    path ('api/register/', views.register_user, name='register_user')

]