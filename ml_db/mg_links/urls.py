from django.urls import path
from .views import AddedView, SearchView, index
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('added/', AddedView.as_view()),
    path('search/', SearchView.as_view()),
    # path('/search' ),
    ]


