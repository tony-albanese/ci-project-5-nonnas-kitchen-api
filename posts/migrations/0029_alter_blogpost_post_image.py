# Generated by Django 3.2.16 on 2023-02-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_auto_20230218_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_image',
            field=models.ImageField(blank=True, default='../blogpost_default_image_v2nwpm', upload_to='images/'),
        ),
    ]
