from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('website.urls')),
    path('admin/', admin.site.urls),
    path('api/',include('ocr_api.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
