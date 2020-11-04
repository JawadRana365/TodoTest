from rest_framework import generics

## import todo form and models
from .models import Todo,User

## import UserSerializer form serializer
from .serializer import UserSerializer,TodoSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer