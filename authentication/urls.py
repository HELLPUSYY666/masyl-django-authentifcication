from django.urls import path, include
from .views import (
    LoginAPIView,
    RegistrationAPIView,
    UserRetrieveUpdateAPIView
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

app_name = 'authentication'

urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user-detail'),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),

    path('auth/', include('djoser.urls')),  # для регистрации, сброса пароля и т.д.
    path('auth/jwt/', include('djoser.urls.jwt')),  # для JWT-токенов
    path('auth/rest-auth/', include('dj_rest_auth.urls')),  # для login/logout с использованием JWT
]
