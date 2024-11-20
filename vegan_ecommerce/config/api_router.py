from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


from apps.users.api.views import LogoutAPIView

router = SimpleRouter()


urlpatterns = [
    path('users/logout/', LogoutAPIView.as_view(), name='logout'),
    path('users/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns += router.urls
