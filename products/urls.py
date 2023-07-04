from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('workshops/', views.workshops, name='workshops'),
    path('workshops/<slug>/', views.workshop_detail, name='workshop_detail'),
    path('digital_products/', views.digital_products, name='digital_products'),
    path('digital_products/<slug>/', views.digital_product_detail,
         name='digital_product_detail'),
    path('add_workshop/', views.add_workshop, name='add_workshop'),
    path('add_digital_product/', views.add_digital_product,
         name='add_digital_product'),
    path('edit_workshop/<slug>/', views.edit_workshop, name='edit_workshop'),
    path('edit_digital_product/<slug>/', views.edit_digital_product,
         name='edit_digital_product'),
    path('delete/<slug>/', views.delete_product, name='delete_product'),
]
