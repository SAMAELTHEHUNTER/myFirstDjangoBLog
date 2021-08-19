from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_home'),
    path('<slug>', views.article_details, name='details'),
]
