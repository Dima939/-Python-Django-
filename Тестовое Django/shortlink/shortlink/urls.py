from django.contrib import admin
from django.urls import path, include
from shortlink_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('home/', views.HomeView.as_view()),
]
