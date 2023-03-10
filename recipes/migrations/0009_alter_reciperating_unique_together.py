# Generated by Django 3.2.16 on 2023-02-12 13:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0008_reciperating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reciperating',
            unique_together={('owner', 'recipe')},
        ),
    ]
