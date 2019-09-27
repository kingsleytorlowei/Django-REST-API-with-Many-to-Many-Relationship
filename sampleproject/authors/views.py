from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import UserSerializer, AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework import filters

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class AuthorViewSet(viewsets.ModelViewSet):
    """
    List all workers, or create a new worker.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    List all workkers, or create a new worker.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['release_date']
    
