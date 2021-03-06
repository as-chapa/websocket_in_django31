from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('channel/', views.ChannelView.as_view(), name='channel'),
]
