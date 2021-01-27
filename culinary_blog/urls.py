from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = "blog"

urlpatterns = [
    path('list/', views.post_list, name = "list"),
    path('list/tag/<slug:tag_slug>/', views.post_list, name = "list_by_tag"),
    path('search/', views.post_search, name="post_search"),
    path('post/', views.create_post, name = 'create_post'),
    path('main_page/', views.main_page,name = "main_pg"),
    path('<slug:name>/', views.get_post_of_category, name = "cat_name"),
    path('<int:post_id>/<slug:name>/', views.post_detail, name = "post_detail"),


]


