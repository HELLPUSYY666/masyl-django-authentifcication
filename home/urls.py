from django.contrib import admin
from django.urls import path, include

import authentication.views
from . import views
from authentication.views import RegistrationAPIView, LoginAPIView
from .views import RegisterView
app_name = 'home'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('add-masyli/', views.AddMasyliView.as_view(), name='add_masyli'),
    path('add-masyly-details/<int:masyli_id>/', views.AddMasylyDetailsView.as_view(), name='add-masyly-details'),
    path('update/<int:pk>/', views.MasyliUpdateView.as_view(), name='update'),
    path('supernatural-list/', views.SupernaturalListView.as_view(), name='supernatural-list'),
    path('masyli-list/', views.MasylyDetailsView.as_view(), name='masyli_list'),
    path('profile', views.profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('success/', views.success_view, name='success'),
]

