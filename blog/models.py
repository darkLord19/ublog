from django.db import models
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.sites.models import Site

class Post(models.Model):
    category_choices = (
        ('technology', 'Technology'),
        ('personal', 'Personal'),
        ('poetry', 'Poetry'),
        ('rants', 'Rants'),
        ('random', 'Random'),
    )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    body = models.TextField()
    summary = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=70, unique=True)
    category = models.CharField(
        max_length=10, choices=category_choices, default='technology'
    )
    tags = models.ManyToManyField('Tag')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def is_published(self):
        if self.published_date is None:
            return False
        return True

    def save(self, *args, **kwargs):
        tmp = str(self.body)
        self.summary = tmp[:100]
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if self.is_published():
            st = '/' + str(self.published_date.year) + '/' + str(self.published_date.month) + '/' + str(self.slug)
            return st
        return

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments'
    )
    author = models.CharField(max_length=15)
    msg = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    comment_visibility = models.BooleanField(default=True)

    def unapprove(self):
        self.comment_visibility = False
        self.save()

    def __str__(self):
        return self.msg

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
