from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from article.models.article import Article
from article.serializers.article import ArticleSerializer


class ArticleListApiView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailApiView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreateApiView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer