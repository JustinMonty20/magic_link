from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('added/', views.added, name='added'),
    # path('search/', views.search, name='search'),
    ]


