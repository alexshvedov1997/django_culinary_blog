# Generated by Django 3.1.5 on 2021-01-23 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('culinary_blog', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]