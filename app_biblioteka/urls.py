from django.urls import path
from . import views

app_name = 'app_biblioteka'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('books/<int:id>/', views.book, name='book'),
    path('book/edit/<int:id>/', views.edit, name='edit'),
    path('book/new/', views.new, name='new')
]
