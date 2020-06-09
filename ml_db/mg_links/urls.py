from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('added/', TemplateView.as_view(template_name='added.htm')),
    path('search/', TemplateView.as_view(template_name='search.htm')),
    ]


