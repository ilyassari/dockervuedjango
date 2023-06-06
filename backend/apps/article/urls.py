from django.contrib import admin
from django.urls import path, include

from article.views.article import ArticleListApiView, ArticleDetailApiView, ArticleCreateApiView


urlpatterns = [
    path("list", ArticleListApiView.as_view(), name="list"),
    path("detail/<int:pk>", ArticleDetailApiView.as_view(), name="detail"),
    path("create", ArticleCreateApiView.as_view(), name="create")
]