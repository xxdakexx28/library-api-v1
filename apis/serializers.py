from rest_framework import serializers
from books.models import book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'