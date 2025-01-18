from django.urls import path

from apps.bytea_image.views import get_image

app_name = 'bytea_image'


urlpatterns = [
    path('bytea-image/<uuid>/', get_image, name='bytea_image'),
]
