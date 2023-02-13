# Generated by Django 3.2.16 on 2023-02-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_alter_blogpost_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('remin', 'Reminiscence'), ('anec', 'Anecdote'), ('fact', 'Fun Fact'), ('tip', 'Tip'), ('orig', 'Origin'), ('hist', 'History')], default='anec', max_length=5),
        ),
    ]
