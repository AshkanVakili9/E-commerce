from django.urls import path
from core.base.views import product_views as views


urlpatterns = [
    
    path('', views.getProducts, name='products'),
    
    path('category/', views.getCategories, name='categories'),
    path('category/<int:pk>/', views.getCategory, name='category-id'),
    path('create_category/', views.createCategory, name='create-category'),
    path('update_category/<int:pk>/', views.updateCategory, name='update-category'),
    path('delete_category/<int:pk>/', views.deleteCategory, name='delete-category'),
    
    path('create/', views.createProduct, name='product-create'),
    path('upload/', views.uploadImage, name='image-upload'),
    
    path('<int:pk>/review/', views.createdProductReview, name='create-review'),
    path('top/', views.getTopProducts, name='top-products'),
    path('<int:pk>/', views.getProduct, name='products'),
    
    path('update/<int:pk>/', views.updateProduct, name='product-update'),
    path('delete/<int:pk>/', views.deleteProduct, name='product-delete'),

]
