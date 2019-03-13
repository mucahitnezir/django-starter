from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin, CreateView, UpdateView

from .models import Post
from .forms import PostForm, CommentForm
from category.models import Category


class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    extra_context = {'title': _('Posts')}
    paginate_by = 5
    page_kwarg = 'page'

    def get_queryset(self):
        posts = Post.objects.all()
        query = self.request.GET.get('q', None)
        if query:
            posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
        return posts

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['categories'] = Category.objects.filter(type='post')
        return data


class PostDetailView(SuccessMessageMixin, FormMixin, DetailView):
    model = Post
    template_name = 'post/detail.html'
    form_class = CommentForm
    success_message = _('Comment is created successfully!')

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = self.object.title
        data['meta_description'] = self.object.meta_description
        return data

    def get_success_url(self):
        return self.object.get_absolute_url()

    def post(self, request, *args, **kwargs):
        # Get object
        self.object = self.get_object()
        # Form actions
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'post/form.html'
    extra_context = {'title': _('Create Post')}
    form_class = PostForm
    success_message = _('Post created successfully')

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'post/form.html'
    extra_context = {'title': _('Create Post')}
    form_class = PostForm
    success_message = _('Post updated successfully!')

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = '{}: {}'.format(_('Update'), self.object.title)
        return data

    def get_success_url(self):
        return self.object.get_absolute_url()


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


class CategoryDetailView(SingleObjectMixin, ListView):
    model = Post
    template_name = 'post/category.html'
    paginate_by = 5

    def get_object(self, queryset=None):
        return get_object_or_404(Category, pk=self.kwargs['id'], slug=self.kwargs['slug'], type='post')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Post.objects.filter(category=self.object)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = self.object.name
        data['meta_description'] = self.object.meta_description
        data['categories'] = Category.objects.all()
        return data
