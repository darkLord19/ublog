from django.utils import timezone
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post

class PostsFeed(Feed):
    title = "U's Posts"
    description_template = "post_detail.html"

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foo'] = 'bar'
        return context

class LatestEntriesFeed(Feed):
    title = "U's Blog"
    link = "/feed/"
    description = "U's Blog"

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by(
            "-published_date")

    def item_title(self, item):
        return item.title

    def item_summary(self, item):
        return item.summary