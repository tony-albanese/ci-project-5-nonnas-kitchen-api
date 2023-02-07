from django.db import models
from posts.models import BlogPost
from base_models.models import AbstractComment

# Create your models here.

class Comment(AbstractComment):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    # TODO must implement likes
    
