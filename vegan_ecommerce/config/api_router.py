from django.urls import path, include

from rest_framework_nested import routers

from djoser.urls import base

from apps.users.api.views import LogoutAPIView
from apps.category.api.views import CategoryViewSet
from apps.subcategory.api.views import SubcategoryViewSet
from apps.mark.api.views import MarkViewSet
from apps.ingredient.api.views import IngredientViewSet
from apps.product.api.views import ProductViewSet
from apps.order.api.views import OrderViewSet


router = routers.SimpleRouter()

router.register('category', CategoryViewSet, 'category')
router.register('subcategory', SubcategoryViewSet, 'subcategory')
router.register('mark', MarkViewSet, 'mark')
router.register('ingredient', IngredientViewSet, 'ingredient')
router.register('product', ProductViewSet, 'product')

user_router = routers.NestedSimpleRouter(base.router, 'users', lookup='user')
user_router.register('order', OrderViewSet, basename='order')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/users/logout/', LogoutAPIView.as_view(), name='logout'),
]

urlpatterns += router.urls
urlpatterns += user_router.urls
