from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# app_name = "fristapp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('', views.Home, name='Home'),
    path ('articles/', include('articles.urls')),
]


urlpatterns += staticfiles_urlpatterns()
