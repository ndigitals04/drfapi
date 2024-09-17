from django.urls import path
from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy, BlogPostList

urlpatterns = [
    path('blogposts/', BlogPostListCreate.as_view(), name="Blogost-viewcreate"),
    path('blogposts/<int:pk>/', BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
    path('blogposts/search/<str:title>/',BlogPostList.as_view(), name="search" ),
]