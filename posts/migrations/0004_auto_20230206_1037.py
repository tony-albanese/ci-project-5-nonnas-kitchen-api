# Generated by Django 3.2.16 on 2023-02-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230205_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='tags',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('anec', 'Anecdote'), ('tip', 'Tip'), ('orig', 'Origin'), ('hist', 'History'), ('fact', 'Fun Fact'), ('remin', 'Reminiscence')], default='anec', max_length=5),
        ),
    ]
