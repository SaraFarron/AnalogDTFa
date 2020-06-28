from django.urls import path
from . import views
from news.models import Articles

urlpatterns = [
    path('', views.index, name='index')
]