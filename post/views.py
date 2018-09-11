from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm, CommentForm
from category.models import Category


def post_index(request):
    categories = Category.objects.filter(type='post')
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(Q(title__icontains=query) |
                                     Q(content__icontains=query) |
                                     Q(user__first_name__icontains=query) |
                                     Q(user__last_name__icontains=query) |
                                     Q(category__name__icontains=query)
                                     ).distinct()

    paginator = Paginator(post_list, 5)  # Show 5 posts on per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'categories': categories,
        'title': 'Blog Yazıları'
    }
    return render(request, 'post/index.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        messages.success(request, 'Comment is created successfully')
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'post': post,
        'form': form,
        'title': post.title
    }
    return render(request, 'post/detail.html', context)


@login_required(login_url='account:login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post created successfully')
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm()

    context = {
        'form': form,
        'title': 'Blog Yazısı Oluştur'
    }
    return render(request, 'post/form.html', context)


@login_required(login_url='account:login')
def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user.is_superuser or post.user == request.user:
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return HttpResponseRedirect(post.get_absolute_url())

        context = {
            'form': form,
            'title': 'Güncelle: ' + post.title
        }
        return render(request, 'post/form.html', context)
    else:
        return redirect('home')


@login_required(login_url='account:login')
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user.is_superuser or post.user == request.user:
        post.delete()
        return redirect('post:index')
    else:
        return redirect('post:index')


def category_detail(request, slug, id):
    category = get_object_or_404(Category, id=id, slug=slug, type='post')
    categories = Category.objects.filter(type='post')
    posts = category.posts.all()
    context = {
        'category': category,
        'categories': categories,
        'posts': posts
    }
    return render(request, 'post/category.html', context)
