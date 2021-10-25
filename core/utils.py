from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class BaseAPIView(APIView):
    serializer_class = Serializer

    def get_serializer_context(self):
        return {'request': self.request, 'view': self}

    def get_serializer_class(self):
        return self.serializer_class

    def get_serializer(self, *a, **kw):
        serializer_class = self.get_serializer_class()
        kw['context'] = self.get_serializer_context()
        return serializer_class(*a, **kw)


def paginate_queryset(qs, size, page):
    p = Paginator(qs, size)
    try:
        qs = p.page(page)
    except PageNotAnInteger:
        qs = p.page(1)
    except EmptyPage:
        qs = []
    return {'num_pages': p.num_pages, 'count': p.count, 'qs': list(qs)}


def success_response(data):
    return {"status": "success", "data": data}