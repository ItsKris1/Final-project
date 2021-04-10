from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_store.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

