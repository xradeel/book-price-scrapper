
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import BooksRecord

@registry.register_document
class BookDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'books'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = BooksRecord  # The model associated with this document
        fields = [
            'title',
            'author',
            'price',
            'url',
            # 'image',
        ]
