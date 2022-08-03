from rest_framework.serializers import ModelSerializer
from shop.models import Category, Product, Article
from rest_framework import serializers


class AdminArticleViewset(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'ecoscore']


class ProductDetailSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category', 'articles']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductListSerializer(queryset, many=True)
        return serializer.data


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError('Cette catégorie existe déjà!')
        return value

    def validate(self, data):
        if data['name'] not in data['description']:
            raise serializers.ValidationError('Les noms doivent posséder une description!')
        return data