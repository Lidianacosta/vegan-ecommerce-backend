from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # ------------------------------------------------------------------------
    # DRF-SPECTACULAR
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # ------------------------------------------------------------------------
    # API
    path('api/', include("config.api_router")),
    # ------------------------------------------------------------------------
    # APPS
    path('bytea-image/', include("apps.bytea_image.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
