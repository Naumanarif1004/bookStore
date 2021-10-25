from rest_framework import serializers

class BookListSerializer(serializers.Serializer):
    search_text = serializers.CharField(required=False, allow_blank=True, trim_whitespace=True)
    size = serializers.IntegerField(required=True)
    page = serializers.IntegerField(required=True)

class BookCreateSerializer(serializers.Serializer):
    writer = serializers.CharField(required=True, trim_whitespace=True)
    name = serializers.CharField(required=True, trim_whitespace=True)
    synopsis = serializers.CharField(required=False, allow_blank=True, trim_whitespace=True)
    genre = serializers.CharField(required=False, allow_blank=True, trim_whitespace=True)
    release_date = serializers.DateField(required=False)
    price = serializers.IntegerField(required=True)