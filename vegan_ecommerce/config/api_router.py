from django.urls import path, include

from rest_framework.routers import SimpleRouter

from apps.users.api.views import LogoutAPIView
from apps.category.api.views import CategoryViewSet

router = SimpleRouter()

router.register('category', CategoryViewSet, 'category')


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/users/logout/', LogoutAPIView.as_view(), name='logout'),
]

urlpatterns += router.urls
