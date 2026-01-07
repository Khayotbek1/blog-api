from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.serializers import UserRetrieveSerializer
from .models import *

class ArticleCreateSerializer(ModelSerializer):
    tags  = serializers.PrimaryKeyRelatedField(many=True,queryset=Tag.objects.all(), required=False)
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {
            'author':{'read_only':True},
            'slug':{'read_only':True},
        }

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        extra_kwargs = {
            'slug':{'read_only':True},
        }

class ArticleRetrieveSerializer(ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    author = UserRetrieveSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

