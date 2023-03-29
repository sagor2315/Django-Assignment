from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView
from .models import *

from .forms import CommentForm
from django.urls import reverse_lazy


# Create your views here.
def home_view(request):
    quaryset = Post.objects.filter(status='publish').order_by('-update_post')
    per_page = 3
    paginator = Paginator(quaryset, per_page)
    page_number = request.GET.get('page')
    Dina_post = paginator.get_page(page_number)
    context = {'Dina_post':Dina_post}
    return render(request, 'blog/index.html', context)



def Blog(request):
    quaryset = Post.objects.filter(status='publish').order_by('-created_post')
    per_page = 3
    paginator = Paginator(quaryset, per_page)
    page_number = request.GET.get('page')
    Dinamic_post = paginator.get_page(page_number)
    context = {'Dinamic_post':Dinamic_post}
    return render(request, 'blog/blog.html', context)

def Tools(request):
    quaryset = Post.objects.filter(status='publish').order_by('-category')
    per_page = 3
    paginator = Paginator(quaryset, per_page)
    page_number = request.GET.get('page')
    tool_post = paginator.get_page(page_number)
    context = {'tool_post':tool_post}
    return render(request, 'blog/tools.html', context)


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    images = post.featured
    recent_posts = Post.objects.order_by('-status')[:10] # Get the 5 latest posts
    context = {
        'post': post,
        'recent_posts': recent_posts,
        'images': images
    }
    return render(request, 'blog/single.html', context)








