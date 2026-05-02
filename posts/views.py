# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from posts.models import Post
from posts.posts import get_posts_filter_by_rate


def home(request):
    post = Post.objects.get(id=1)
    return HttpResponse(f"<h1>Text</h1>  ---- {post.title} <br> {post.content}")


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "base.html", {"post": post})

def posts(request):
    posts = get_posts_filter_by_rate(2)

    return render(request, template_name="base.html", context={"posts": posts})

def get_posts_by_category(request, id):
    posts = Post.objects.filter(category_id=id)

    return render(request, template_name="posts/posts.html", context={"posts": posts})

def post_list(request):
    posts = Post.objects.filter(is_published=True, rating__gt=5)

    return render(request, 'posts/post_list.html', {
        'posts': posts
    })

