from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.all_shops, name='all_shops'),
    path('about/<int:id>', views.about_shop, name='about_shop'),
    path('create_goods/', views.add_goods, name='create_goods'),
    path('create_shop/', views.add_shop, name='create_shop'),
    path('delete_goods/<int:id>', views.delete_goods, name='delete_goods'),
    path('delete_shop/<int:id>', views.delete_shop, name='delete_shop'),
    path('update_shop/<int:id>', views.update_shop, name='update_shop'),
    path('update_goods/<int:id>', views.update_goods, name='update_goods'),
]