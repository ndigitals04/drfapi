from django.urls import path
from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy, BlogPostList, BlogPostCreate

urlpatterns = [
    path('blogposts/', BlogPostListCreate.as_view(), name="Blogost-viewcreate"),
    path('blogposts/<int:pk>/', BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
    path('blogposts/search/<str:title>/',BlogPostList.as_view(), name="search" ),
    path('blogposts/create',BlogPostCreate.as_view(), name="create"),
]