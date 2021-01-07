from django.urls import path
from . import views

app_name = 'app_biblioteka'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:id>/', views.article, name='article'),
    path('article/edit/<int:id>/', views.edit, name='edit'),
    path('article/new/', views.new, name='new')
]
