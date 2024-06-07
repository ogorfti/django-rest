from .models import Todo
from .serializers import TodoSerializer
from rest_framework import generics


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # lookup_field = 'pk'