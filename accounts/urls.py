from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.singup_page, name='signup'),
    path('signin/', views.signin_page, name='signin'),
]
