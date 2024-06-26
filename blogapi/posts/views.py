from .serializers import PostSerializer, UserSerializer
from .models import Post
from rest_framework import generics, permissions, viewsets
from .permissions import testSec
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [testSec, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 2nd method
# class PostViewSet(viewsets.ModelViewSet):
#     permission_classes = [testSec, ]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer