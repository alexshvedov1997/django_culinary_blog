from django.shortcuts import render, get_object_or_404
from .models import CulinaryPost, Category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
from .forms import  CommentForm, CulinaryPostForm, SearchForm
from django.contrib.postgres.search import  SearchVector

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
    #comment = post.comments.all()
    all_object = post.comments.all()
    object_list = post.comments.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    try:
        comment = paginator.page(page)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment= paginator.page(paginator.num_pages)

    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit= False)
            new_comment.post = post
            new_comment.name = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,"blog/post/culinary_post.html", {"post":post, 'comments':comment,
                                                           'new_comment': new_comment,
                                                           'comment_form':comment_form, 'page':page,
                                                           'all_object':all_object} )

def create_post(request):
    categories = Category.objects.all()
    new_post= None
    if request.method == 'POST':
        post_form = CulinaryPostForm(data = request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit = False)
            new_post.author = request.user
            new_post.save()
            return render(request,'blog/main_pg/main_menu.html', {"categories":categories})
    else:
        post_form = CulinaryPostForm()
    return render(request, 'blog/post/create_post.html', {'new_post':new_post, 'post_form':post_form})

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = CulinaryPost.objects.annotate(search = SearchVector('title','body'),).filter(search = query)
    return render(request,"blog/post/search.html", {'form':form,'query':query,'results':results})



