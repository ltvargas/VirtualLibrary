from django.contrib import admin
from django.urls import path
from biblioteca import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('load_books/', views.load_books),
    path('search_books/<code>', views.search_books),
    path('create_book/', views.create_book),
    path('borrow_history/<user>', views.borrow_history),
    path('return_book/', views.return_book),
    path('load_borrow/<user>', views.load_borrow),
    path('reserver_book/', views.reserver_book),
    path('unreserver_book/', views.unreserver_book),
    path('borrow_book/', views.borrow_book),
]
