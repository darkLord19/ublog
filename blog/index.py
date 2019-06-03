from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Post

@register(Post)
class PostIndex(AlgoliaIndex):
	fileds = ('title', 'body', 'tags', 'categories')

	settings = {
		'searchableAttributes': ['title', 'body', 'tags'],
		'queryType': 'prefixAll',
		'highlightPreTag': '<mark>',
		'highlightPostTag': '</mark>',
		'hitsPerPage': 15
	}
