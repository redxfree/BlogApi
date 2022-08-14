
from django.shortcuts import redirect
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.serializers import AuthTokenSerializer
from blogs.models  import *
from blogs.serializers import *
from rest_framework.response import Response
from django.contrib.auth import logout 

class BlogList(generics.ListAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer


class Blogdetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

class Blog(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
   
			
	
class Category(generics.CreateAPIView):
	queryset = category.objects.all()
	serializer_class = categorySerializers
	
	
	

class CategoryList(generics.ListAPIView):
	queryset = category.objects.all()
	serializer_class = categorySerializers
	
	
	
class CommentList(generics.CreateAPIView):
	queryset = comment.objects.all()
	serializer_class  = commentSerializers
	
	

