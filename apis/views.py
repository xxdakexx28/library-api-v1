from rest_framework import generics
from books.models import book

from .serializers import BookSerializer

# Create your views here.


class BookApiView(generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer