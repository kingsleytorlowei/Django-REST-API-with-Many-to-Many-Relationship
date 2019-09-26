from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework import status, response
from .models import Author, Book


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

       
class AuthorSerializer(serializers.ModelSerializer):
    depth = 1

    class Meta:
        ordering = ['-id']
        model = Author
        fields = ("id", "name", "biography", "date_of_birth", "books")


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Book
        fields = ("id", "title", "description", "publisher", "release_date", "authors")
        extra_kwargs = {'authors': {'required': False}}
        depth = 1
