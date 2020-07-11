from django.shortcuts import render,get_object_or_404
from .models import Blog

def index(request):
    blogs = Blog.objects
    return render(request,'index.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk = blog_id)
    return render(request,'detail.html',{'blog':blog_detail})
    