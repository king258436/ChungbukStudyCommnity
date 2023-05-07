from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Post, Comment

def bulletinBoard(request):
    if request.method == 'POST':
        # Handle form submission to create a new post
        post_title = request.POST.get('title')
        post_content = request.POST.get('content')
        post_author = request.POST.get('author')
        post_lect_name = request.POST.get('lectName')
        post = Post.objects.create(
            title=post_title,
            content=post_content,
            author=post_author,
            lectName=post_lect_name
        )
        return redirect('bulletinBoard')

    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'Board.html', {
        'posts' : posts
    })
