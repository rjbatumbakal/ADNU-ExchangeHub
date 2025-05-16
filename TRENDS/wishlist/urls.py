from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist_view, name='wishlist'),  # /wishlist (no trailing slash)
    path('add', views.add_to_wishlist, name='add_to_wishlist'),  # /wishlist/add
    path('remove/<int:item_id>', views.remove_from_wishlist, name='remove_from_wishlist'),  # /wishlist/remove/1
    path('addtocart/<int:item_id>', views.add_wishlist_to_cart, name='add_wishlist_to_cart'),  # /wishlist/addtocart/1
    path('', views.wishlist_view, name='wishlist'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

]
