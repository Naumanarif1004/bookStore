from django.shortcuts import render
from .utils import BaseAPIView,paginate_queryset,success_response
from .serializers import BookListSerializer,BookCreateSerializer
from rest_framework.response import Response
from .models import Book
from django.db.models import Q
from functools import reduce
import operator

class BookListFilter(BaseAPIView):
    serializer_class = BookListSerializer

    def post(self, request, *a, **kw):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if serializer.data['search_text'] == '' or serializer.data['search_text'] == None:
                qs = list(Book.objects.all().order_by('-created_at').values())
            else:
                serach_queries = serializer.data['search_text'].split()
                qset1 = reduce(operator.__or__,
                               [
                                   Q(writer__icontains=query)
                                   | Q(name__icontains=query)
                                   | Q(synopsis__icontains=query)
                                   | Q(genre__icontains=serializer.data['search_text'])
                                   | Q(price__icontains=serializer.data['search_text']) for query in serach_queries
                               ])
                qs = list(Book.objects.filter(qset1).order_by('-created_at').values())

            sizeOfpage = serializer.data['size']
            if (sizeOfpage == 0):
                sizeOfpage = 50

            data = paginate_queryset(qs, sizeOfpage, serializer.data['page'])
            return Response(success_response(data))
        return Response(serializer.errors)

class BookCreate(BaseAPIView):
    serializer_class = BookCreateSerializer

    def post(self, request, *a, **kw):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                Book.objects.create(
                    writer=serializer.data['writer'],
                    name=serializer.data['name'],
                    synopsis=serializer.data['synopsis'],
                    genre=serializer.data['genre'],
                    release_date=serializer.data['release_date'],
                    price=serializer.data['price']
                )
            except Exception as exc:
                return Response(str(exc))
            return Response(success_response('Created'))
        return Response(serializer.errors)