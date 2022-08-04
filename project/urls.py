from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from shop.serializers import AdminArticleViewset
from shop.views import CategoryViewset, ProductViewset, ArticleViewset, AdminCategoryViewset
from rest_framework import routers

router = routers.SimpleRouter()

router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')
router.register('admin/category', AdminCategoryViewset, basename='admin-category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_pair_obtain'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
