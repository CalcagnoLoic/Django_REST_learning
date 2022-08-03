from django.contrib import admin
from django.urls import path, include
from shop.views import CategoryViewset, ProductViewset, ArticleViewset
from rest_framework import routers

router = routers.SimpleRouter()

router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
