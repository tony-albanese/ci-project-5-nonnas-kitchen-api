from django.db import models
from kitchen_user.models import User

# Create your models here.


class Follower(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-followed_on']
        unique_together = ['following', 'follower']

    def __str__(self):
        return f'{self.following} {self.follower}'
