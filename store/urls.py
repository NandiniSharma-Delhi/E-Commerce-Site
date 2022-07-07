from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('login_user/', views.login_user, name="login_user"),
    path('register_user/', views.register_user, name="register_user"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('test/', views.test, name="test"),
    path('add_product/', views.addProduct, name="add_product"),
    path('men/', views.men, name="men"),
    path('women/', views.women, name="women"),
    path('kids/', views.kids, name="kids"),
    path('furniture/', views.furniture, name="furniture"),
    path('electronics/', views.electronics, name="electronics"),
    path('books/', views.books, name="books"),

    path('view_product/<int:id>', views.view_product, name="view_product"),
]
