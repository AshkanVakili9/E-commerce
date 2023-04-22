from django.urls import path
from .views import *


urlpatterns = [

    path('products/', getProducts, name='products'),
    path('products/<int:pk>', getProduct, name='products'),

]
