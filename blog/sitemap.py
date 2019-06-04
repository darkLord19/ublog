from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from .models import Post

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date'
        )

    def lastmod(self, obj):
        return obj.published_date

SITEMAPS = {
    'post': PostSitemap
}
