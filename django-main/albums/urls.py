from django.urls import path, include
#from albums.views import(ArticleView, TagView, CategoryView)
from .views import (CategoryView, TagView, ArticleView)




urlpatterns = [
    #ArticleView
    path('articles/', ArticleView.as_view({'get': 'list', 'post': 'create'}), name = 'Article List'),
    path('articles/<int:id>',ArticleView.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'}), name = 'Article Delete'),

    #TagView
    path('tags/', TagView.as_view({'get': 'list', 'post': 'create'}), name = 'Tag List'),
    path('tags/<int:id>',TagView.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'}), name = 'Tag Delete'),

    #CategoryView
    path('categories/', CategoryView.as_view({'get': 'list', 'post': 'create'}), name = 'Category List'),
    path('categories/<int:id>', CategoryView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'}), name = 'Category Detail'),
]


