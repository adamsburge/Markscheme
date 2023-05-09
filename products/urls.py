from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('workshops/', views.workshops, name='workshops'),
    path('workshops/<slug>', views.workshop_detail, name='workshop_detail'),
    path('digital_products/', views.digital_products, name='digital_products'),
    path('digital_products/<slug>', views.digital_product_detail, name='digital_product_detail'),
]
