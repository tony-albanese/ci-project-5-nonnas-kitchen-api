from django.db import models
from kitchen_user import User


class Profile(models.Model):
    SPECIALTY_CHOICES = [
        ('DES', 'Dessert'),
        ('MEAT', 'Meats'),
        ('GRILL', 'Grilling'),
        ('VEG', 'Vegetables'),
        ('BREAK', 'Breakfast'),
        ('NO', 'Nothing Really'),
        ('ALL', 'A little of everything')
    ]

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    specialty = models.CharField(max_length=5, choices=SPECIALTY_CHOICES, default='NO')
    avatar = models.ImageField(upload_to='images/', default='../default_avatar_kaw1ox')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"