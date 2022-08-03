from django.contrib import admin
from django.urls import path, include

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
    path('api/', include(router.urls))
]
