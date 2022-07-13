from django.contrib import admin
from django.urls import path, re_path, include
from shortlink_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('home/', views.HomeView.as_view()),
    re_path(r'links/(?P<id>\d+)', views.LinksView.as_view()),
]
