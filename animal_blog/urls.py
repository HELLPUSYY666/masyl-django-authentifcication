from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from authentication import views as auth_views
from home.views import RegisterView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls', namespace='authentication')),
    path('', home_views.main_page, name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', home_views.login_view, name='login'),
    path('profile/', home_views.profile_view, name='profile'),
    path('register', RegisterView.as_view(), name='register'),

    path('about/', home_views.about_page, name='about-us'),
    path('levels-confirm/', home_views.levels_confirm, name='levels-confirm'),
    path('add-masyli/', home_views.AddMasyliView.as_view(), name='add-masyli'),
    path('supernatural-list/', home_views.SupernaturalListView.as_view(), name='supernatural-list'),
    path('update/<int:pk>/', home_views.MasyliUpdateView.as_view(), name='update'),
    path('masyli-list/', home_views.MasylyDetailsView.as_view(), name='masyli_list'),
    path('add-masyly-details/<int:masyli_id>/', home_views.AddMasylyDetailsView.as_view(), name='add-masyly-details'),
    path('success/', home_views.success_view, name='success'),
    path('__debug__/', include('debug_toolbar.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
