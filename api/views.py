from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

class BlogPostList(APIView):
    def get(self, request,title, format=None):
        # title = request.query_params.get("title", "teeth")
        if title:
            print(title + "is present")
            blogposts = BlogPost.objects.filter(title__icontains=title)
        else:
            print("not present")
            blogposts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blogposts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogPostCreate(APIView):
    def post(self,request, format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            BlogPost.objects.create(title=request.data["title"], content=request.data["content"])
            return Response({"BlogPost created": serializer.data})