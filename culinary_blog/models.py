from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Категория")
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('category_name',)

    def get_absolute_url(self):
        return  reverse('blog:cat_name', args=[self.slug,])



class CulinaryPost(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'culinary_post', verbose_name="Автор")
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    culinary_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categoryName", verbose_name="Категория")
    photo = models.ImageField(upload_to='blog_photo/', blank=True, verbose_name="Картинка")
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return  reverse('blog:post_detail', args=[self.id, self.slug,])

class Comment(models.Model):
    post = models.ForeignKey(CulinaryPost, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_name', verbose_name="Автор")
    body = models.TextField(verbose_name="Текст")
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    class Meta:
        ordering = ('-publish',)


# Create your models here.
