from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    body = models.TextField()
    summary = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        tmp = str(self.body)
        self.summary = tmp[:100]
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=15)
    msg = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    comment_visibility = models.BooleanField(default=True)

    def unapprove(self):
        self.comment_visibility = False
        self.save()

    def __str__(self):
        return self.msg