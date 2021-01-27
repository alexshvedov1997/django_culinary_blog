from django.urls import path
from . import views
app_name = 'api'

urlpatterns = [
    path('subjects/', views.CategoryListView.as_view(), name = 'category_list'),
    path('subjects/<pk>/', views.CategoryDetailView.as_view(), name = 'category_detail')
]