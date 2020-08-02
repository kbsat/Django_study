from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Blog


def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def post(request):
    return render(request,'post.html')

def create(request):
    blog = Blog()
    blog.title= request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk = blog_id)

    return render(request,'detail.html',{'blog':blog_detail})