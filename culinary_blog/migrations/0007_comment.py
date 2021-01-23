# Generated by Django 3.1.5 on 2021-01-23 10:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('culinary_blog', '0006_culinarypost_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=datetime.datetime(2021, 1, 23, 10, 48, 7, 351118, tzinfo=utc))),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_name', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='culinary_blog.culinarypost')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
