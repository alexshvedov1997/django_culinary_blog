# Generated by Django 3.1.5 on 2021-01-25 18:33

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('culinary_blog', '0011_auto_20210125_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culinarypost',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
