# Generated by Django 3.1.5 on 2021-01-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culinary_blog', '0005_auto_20210116_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='culinarypost',
            name='photo',
            field=models.ImageField(blank=True, upload_to='blog_photo'),
        ),
    ]