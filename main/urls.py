from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ArticleCreateAPIView.as_view()),
    path('all/', ArticleListAPIView.as_view()),
    path('my-articles/', MyArticleListAPIView.as_view()),
    path('<slug:slug>/', ArticleRetrieveAPIView.as_view()),
    path('tags/', TagCreateListAPIView.as_view()),
]