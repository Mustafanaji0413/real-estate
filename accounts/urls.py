from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('admin_create', views.createListing, name='admin_create'),
    path('admin_update <str:pk>', views.UpdateListing, name='admin_update'),
    path('admin_delete <str:pk>', views.deleteListing, name='admin_delete'),

    ]
