from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blog_count = Blog.objects.count
    blog = Blog.objects.all()[:5]
    return render(request, 'app_blog/all_blogs.html', {'blog':blog, 'blog_count':blog_count})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'app_blog/detail.html', {'blog':blog})
