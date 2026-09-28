from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category

from django.utils import timezone


def published_posts():
    return Post.objects.select_related(
        'author', 'location', 'category'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True)

def index(request):
    template = 'blog/index.html'

    post_list = published_posts()[:5]

    context = {
        'post_list': post_list
    }
    return render(request, template, context)


def category_posts(request, slug):
    template = 'blog/category.html'

    category = get_object_or_404(
        Category, slug=slug, is_published=True)

    post_list = published_posts().filter(
        category=category)

    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'

    post = get_object_or_404(published_posts(), pk=pk)

    context={'post': post}
    return render(request, template, context)