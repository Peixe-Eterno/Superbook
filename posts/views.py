from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def show_posts(request):

    return render(request, 'posts/lista_posts.html', {'posts': Post.objects.all()})


def criar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()

    return render(request, "posts/form_post.html", {"form": form})