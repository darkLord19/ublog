from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Post

@register(Post)
class PostIndex(AlgoliaIndex):
	fileds = ('title', 'body', 'tags')
	