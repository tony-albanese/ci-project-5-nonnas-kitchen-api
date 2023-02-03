from django.db import models
from kitchen_user.models import User

# Create your models here.


class BlogPost(models.Model):
    TAGS = {
        'anec': 'Anecdote',
        'tip': 'Tip',
        'hist': 'History',
        'fact': 'Fun Fact',
        'orig': 'Origin',
        'remin': 'Reminiscence'
    }

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    body = models.TextField()
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    ratings = models.ManyToManyField(User, blank=True, related_name='post_ratings')
    posted_on = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to='images/', default='../blogpost_default_image_v2nwpm')

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
    def average_rating(self):
        return Rating.objects.filter(blog_post=self).aggregate(Avg("rating")["rating__avg"])


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.blog_post.title}: {self.rating}"

