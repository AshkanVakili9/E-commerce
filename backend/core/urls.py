
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('core.user.urls')),
    path('api/', include('core.base.urls')),
]
