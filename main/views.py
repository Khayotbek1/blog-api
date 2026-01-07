from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import *

class TagCreateListAPIView(APIView):
    def get (self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post (self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.order_by('-created_at')
        serializer = ArticleRetrieveSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleRetrieveAPIView(APIView):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        serializer = ArticleRetrieveSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.filter(author=request.user).order_by('-created_at')
        serializer = ArticleRetrieveSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
