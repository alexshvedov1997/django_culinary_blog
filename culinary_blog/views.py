from django.shortcuts import render, get_object_or_404
from .models import CulinaryPost, Category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def main_page(request):
    categories = Category.objects.all()
    return render(request,'blog/main_pg/main_menu.html', {"categories":categories})

def post_list(request):
    object_all = CulinaryPost.objects.all()
    paginator = Paginator(object_all,1)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        post = paginator.page(1)
    return render(request, "blog/post/list.html", {"post":post, "page":page})

def get_post_of_category(request, name):
    cat = Category.objects.filter(slug = name).first()
    object_list = CulinaryPost.objects.filter(culinary_category_id = cat.id)
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts= paginator.page(paginator.num_pages)

    return  render(request, "blog/post/post_per_category.html", {"posts" : posts,'page':page})

def post_detail(request, post_id, name):
    #post = get_object_or_404(CulinaryPost, id = post_id, slug = name)
    post = CulinaryPost.objects.filter(id = post_id).first()
    return render(request,"blog/post/culinary_post.html", {"post":post} )
