from .serializers import PostSerializer
from .models import Post
from rest_framework import generics, permissions
from .permissions import testSec

class PostList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [testSec, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer