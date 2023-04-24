from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/products/', include('core.base.urls.product_urls')),
    path('api/users/', include('core.base.urls.users_urls')),
    path('api/orders/', include('core.base.urls.orders_urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
