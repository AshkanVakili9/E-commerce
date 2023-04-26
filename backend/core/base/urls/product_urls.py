from django.urls import path
from core.base.views import product_views as views


urlpatterns = [
    
    path('', views.getProducts, name='products'),
    
    path('create/', views.createProduct, name='product-create'),
    path('upload/', views.uploadImage, name='image-upload'),
    
    path('<int:pk>/review/', views.createdProductReview, name='create-review'),
    path('top/', views.getTopProducts, name='top-products'),
    path('<int:pk>/', views.getProduct, name='products'),
    
    path('update/<int:pk>/', views.updateProduct, name='product-update'),
    path('delete/<int:pk>/', views.deleteProduct, name='product-delete'),

]
