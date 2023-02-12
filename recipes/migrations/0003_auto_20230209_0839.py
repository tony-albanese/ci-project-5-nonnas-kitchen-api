# Generated by Django 3.2.16 on 2023-02-09 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_auto_20230208_1348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipelike',
            options={},
        ),
        migrations.AddField(
            model_name='recipelike',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_likes', to='recipes.recipe'),
        ),
        migrations.AddField(
            model_name='reciperating',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
        ),
        migrations.AlterUniqueTogether(
            name='recipelike',
            unique_together={('owner', 'recipe')},
        ),
    ]
