from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('order/', views.order, name='order'),
    path('order/confirm/<int:order_id>/', views.order_confirm, name='order_confirm'),
    path('contact/', views.contact, name='contact'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('about/', views.about, name='about'),

    path('book_table/', views.book_table, name='book_table'),
    
]
