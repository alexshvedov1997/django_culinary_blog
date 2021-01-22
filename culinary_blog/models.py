from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('category_name',)

    def get_absolute_url(self):
        return  reverse('blog:cat_name', args=[self.slug,])



class CulinaryPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'culinary_post')
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    culinary_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categoryName")
    photo = models.ImageField(upload_to='blog_photo', blank=True)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return  reverse('blog:post_detail', args=[self.id, self.slug,])



# Create your models here.
