# Generated by Django 3.2.16 on 2023-02-12 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0007_delete_reciperating'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ratings', to='recipes.recipe')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
