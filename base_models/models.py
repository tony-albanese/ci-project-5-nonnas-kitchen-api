from django.db import models
from kitchen_user.models import User
# Create your models here.


class AbstractComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        abstract = True
        ordering = ['-created_on']

    def __str__(self):
        return self.body


class AbstractLike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_on']


class AbstractRating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_on']