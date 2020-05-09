from libapi.models import Publicationhouse, Book
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'price', 'pages')

class PublicationhouseSerializer(ModelSerializer):
    # book_set = BookSerializer(many=True)
    book_set = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Publicationhouse
        fields = ('id', 'name', 'ratings', 'book_set')