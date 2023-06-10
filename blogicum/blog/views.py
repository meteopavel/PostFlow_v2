from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.db.models.functions import Now

from blog.models import Post, Category


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.select_related(
            'author',
            'location',
            'category'
        ).filter(
            pub_date__lte=Now(),
            is_published=True,
            category__is_published=True
        ).order_by(
            '-pub_date'
        )[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'author',
            'location',
            'category'
        ).filter(
            pub_date__lte=Now(),
            is_published=True,
            category__is_published=True
        ),
        pk=post_id
    )
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(
            is_published=True,
        ),
        slug=category_slug
    )
    post_list = get_list_or_404(
        Post.objects.select_related(
            'author',
            'location',
            'category'
        ).filter(
            pub_date__lte=Now(),
            is_published=True,
            category__slug=category_slug
        )
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template_name, context)
