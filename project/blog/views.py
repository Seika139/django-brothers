from django.shortcuts import render
from .models import Blog

def index(request):
    blog = Blog.objects.order_by('-created_datetime')
    return render(request, 'blog/index.html', {'blog': blog})

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})
