from django.urls import path, re_path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('web/', views.web, name='web'),
    path('games/', views.games, name='games'),
    path('scripts/', views.scripts, name='scripts'),
    path('another/', views.another, name='another'),
    path('<int:pk>/', views.detail, name='detail'),
    re_path('create/', views.create_new_project, name='create_new_project'),
]