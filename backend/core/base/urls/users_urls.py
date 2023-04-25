from django.urls import path
from core.base.views import users_views as views



urlpatterns = [
    
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),


    path('register/', views.registerUser, name='register'),
    
    path('profile/', views.getUserProfile, name='user-profile'),
    path('profile/update/', views.updateUserProfile, name='user-profile-update'),
    path('', views.getUsers, name='users'),
]