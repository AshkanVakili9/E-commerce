from django.urls import path
from core.base.views import product_views as views


urlpatterns = [
    
    path('', views.getProducts, name='products'),
    path('<int:pk>/', views.getProduct, name='products'),

]
