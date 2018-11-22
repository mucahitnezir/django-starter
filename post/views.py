from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.utils.translation import ugettext as _

from .models import Post
from .forms import PostForm, CommentForm
from category.models import Category


def post_index(request):
    # Get all blog categories
    categories = Category.objects.filter(type='post')

    # Get posts with pagination
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

    # Page context
    context = {
        'title': _('Posts'),
        'posts': posts,
        'categories': categories
    }
    # Render page
    return render(request, 'post/index.html', context)


def post_detail(request, slug):
    # Get post
    post = get_object_or_404(Post, slug=slug)
    # Create comment form
    form = CommentForm(request.POST or None)
    # If form is valid, save it
    if form.is_valid():
        messages.success(request, _('Comment is created successfully'))
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    # Page context
    context = {
        'title': post.title,
        'meta_description': post.meta_description,
        'post': post,
        'form': form
    }
    # Render page
    return render(request, 'post/detail.html', context)


@login_required
def post_create(request):
    # Save form or create form instance
    if request.method == 'POST':
        # Set post variables to form
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, _('Post created successfully'))
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm()
    # Page context
    context = {
        'title': _('Create Post'),
        'form': form
    }
    # Render page
    return render(request, 'post/form.html', context)


@login_required
def post_update(request, id):
    # Get post
    post = get_object_or_404(Post, id=id)
    # Security control
    if request.user.is_superuser or post.user == request.user:
        # Create form and if it is valid, save it
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, _('Post updated successfully!'))
            return HttpResponseRedirect(post.get_absolute_url())
        # Page context
        context = {
            'title': _('Update') + ': ' + post.title,
            'form': form
        }
        # Render page
        return render(request, 'post/form.html', context)
    else:
        return redirect('home')


@login_required
def post_delete(request, id):
    # Get post
    post = get_object_or_404(Post, id=id)
    # Security control
    if request.user.is_superuser or post.user == request.user:
        post.delete()
        return redirect('post:index')
    else:
        return redirect('post:index')


def category_detail(request, slug, id):
    # Get category
    category = get_object_or_404(Category, id=id, slug=slug, type='post')
    # Get all blog categories
    categories = Category.objects.filter(type='post')
    # Get all category posts
    posts = category.posts.all()
    # Page context
    context = {
        'title': category.name,
        'meta_description': category.meta_description,
        'category': category,
        'categories': categories,
        'posts': posts
    }
    # Render page
    return render(request, 'post/category.html', context)
