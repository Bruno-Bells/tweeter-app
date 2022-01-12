from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('tweet-list/', views.tweetList, name='tweet-list'),
    path('tweet-create/', views.tweetCreate, name='tweet-create'),
    path('tweet-delete/', views.tweetDelete, name='tweet-delete'),

    path('handle-list/', views.handleList, name='handle-list'),
    path('interval/', views.intervalList, name='interval'),
]