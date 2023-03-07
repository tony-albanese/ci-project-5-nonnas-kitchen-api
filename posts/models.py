from django.db import models
from kitchen_user.models import User
from base_models.models import AbstractLike, AbstractRating
from taggit.managers import TaggableManager
# Create your models here.


class BlogPost(models.Model):
    CATEGORIES = [
        ('anec', 'Anecdote'),
        ('tip', 'Tip'),
        ('hist', 'History'),
        ('fact', 'Fun Fact'),
        ('orig', 'Origin'),
        ('remin', 'Reminiscence')
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to='images/', default='../blogpost_default_image_v2nwpm', blank=True)
    category = models.CharField(max_length=5, choices=CATEGORIES, default='anec')

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title


class Like(AbstractLike):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ['owner', 'blog_post']
        ordering = ['-created_on']

    def __str__(self):
        return f"Owner: {self.owner} Blog Post: {self.blog_post.title}"
