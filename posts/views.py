# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


def home(request):
    post = Post.objects.get(id=1)
    return HttpResponse(f"<h1>Text</h1>  ---- {post.title} <br> {post.content}")


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "base.html", {"post": post})


def posts(request):
    posts = get_posts_filter_by_rate(2)

    return render(request, template_name="base.html", context={"posts": posts})