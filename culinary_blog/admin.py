from django.contrib import admin
from .models import CulinaryPost, Category, Comment

# Register your models here.
@admin.register(Category)
class CulinaryCategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name','slug')

@admin.register(CulinaryPost)
class CulinaryPostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish', 'culinary_category','photo')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'name', 'post', 'publish')






