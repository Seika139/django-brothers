from django.shortcuts import render
from .models import Blog

def index(request):
    blog = Blog.objects.order_by('-created_datetime')
    return render(request, 'blog/index.html', {'blog': blog})
