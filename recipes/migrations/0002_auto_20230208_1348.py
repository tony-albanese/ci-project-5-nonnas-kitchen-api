# Generated by Django 3.2.16 on 2023-02-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-posted_on']},
        ),
        migrations.AddField(
            model_name='recipe',
            name='posted_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
