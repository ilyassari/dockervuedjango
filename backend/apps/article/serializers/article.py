from rest_framework import serializers

from article.models.article import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        depth = 1