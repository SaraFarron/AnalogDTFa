#-*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:pk>/', views.DetailView.as_view(), name='detail'),
    path('<slug:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<poll_id>/vote/', views.vote, name='vote')
]


#path('polls/', include('polls.urls'))


    #path('<slug:pk>/', DetailView.as_view(model=Articles, 
   # template_name="news/post.html")),