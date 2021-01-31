from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('subjects/', views.CategoryListView.as_view(), name = 'category_list'),
    path('subjects/<pk>/', views.CategoryDetailView.as_view(), name = 'category_detail'),
    path('post_list/', views.PostListView.as_view(), name='post_all'),
 #   path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name = 'detail')
    path('post_detail/<int:pk>/', views.PostDetailViewGeneric.as_view(), name = 'detail'),
    path('create_post/', views.CreatePostView.as_view(), name = "new_post")
]