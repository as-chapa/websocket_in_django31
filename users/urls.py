from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('test/', views.IndexView.as_view(), name='index'),
]