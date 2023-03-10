# Generated by Django 3.2.16 on 2023-02-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_alter_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('orig', 'Origin'), ('hist', 'History'), ('remin', 'Reminiscence'), ('anec', 'Anecdote'), ('tip', 'Tip'), ('fact', 'Fun Fact')], default='anec', max_length=5),
        ),
    ]
