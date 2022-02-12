from django.urls import path
from .views import (
    ArticleList,
    ArticleDetail,
    ArticlePreview,
    CategoryList,
    SearchList,
    AuthorList,
)

app_name = 'article'
urlpatterns = [

    path('preview/<int:pk>', ArticlePreview.as_view(), name="article-preview"),
    path('list', ArticleList.as_view(), name="article_list"),
    path('page/<int:page>', ArticleList.as_view(), name="article_list"),
    path('article/<slug:slug>', ArticleDetail.as_view(), name="article-detail"),
    path('category/<slug:slug>', CategoryList.as_view(), name="article_category_list"),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="article_category_list"),
    path('search/', SearchList.as_view(), name="search"),
    path('search/page/<int:page>', SearchList.as_view(), name="search"),
    path('author/<slug:username>', AuthorList.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author"),

]
