from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from shop.models import Category, Product, Article
from shop.permissions import IsAdminAuthenticated
from shop.serializers import CategoryDetailSerializer, CategoryListSerializer, \
    ProductListSerializer, ProductDetailSerializer, AdminArticleViewset

from rest_framework.permissions import IsAuthenticated


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class CategoryViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()


class ProductViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()


class ArticleViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = AdminArticleViewset

    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        article_id = self.request.GET.get('article_id')
        if article_id is not None:
            queryset = queryset.filter(article_id=article_id)
        return queryset


class AdminCategoryViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return Category.objects.all()
