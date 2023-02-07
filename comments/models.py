from django.db import models
from posts.models import BlogPost
from kitchen_user.models import User
# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    # TODO must implement likes


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.body
    
