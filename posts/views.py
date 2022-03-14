from django.shortcuts import render
from .models import Post


def post_comment_create_and_list_view(request):
    posts = Post.objects.all()

    context = {
        'qs': posts
    }

    return render(request, 'posts/main.html', context)
