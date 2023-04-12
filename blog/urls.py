from django.urls import path
from .views import home, api, ArticleList, ArticleDetail,CategoryList

app_name = "blog"
urlpatterns = [
    path('/', home, name="home"),
    # path('home', home_from_database, name="home_from_database"),
    path('',ArticleList.as_view(), name="home_from_database"),
    # path('home/page/<int:page>', home_from_database, name="home_from_database"),
    # path('article/<slug:slug>', detail_article, name="detail"),
    path('article/<slug:slug>', ArticleDetail.as_view(), name="detail"),
    # path('category/<slug:slug>', category, name="category"),
    path('category/<slug:slug>', CategoryList.as_view(), name="category"),
    path('api', api, name="api")
]
