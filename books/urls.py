from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('search/', views.search_books, name='search_books'),
    path('filter_books/', views.filter_books, name='filter_books'),
    path('filtered_results/', views.filtered_results, name='filtered_results'),
    path('delete_filtered_books/', views.delete_filtered_books, name='delete_filtered_books'),
    path('add_author/', views.add_author, name='add_author'),
]
