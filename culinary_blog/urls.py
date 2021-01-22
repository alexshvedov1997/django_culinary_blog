from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "blog"

urlpatterns = [
    path('main_page/', views.main_page,name = "main_pg"),
    path('list/', views.post_list, name = "list"),
    path('<slug:name>/', views.get_post_of_category, name = "cat_name"),
    path('<int:post_id>/<slug:name>/', views.post_detail, name = "post_detail")

]
