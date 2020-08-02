from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.core.paginator import Paginator
from django.utils import timezone


def home(request):
    blogs = Blog.objects
    # 블로그 모든 글을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 짜르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 몇 인지를 알아내고
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해준다.
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})


def post(request):
    return render(request, 'post.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/blog/' + str(blog.id))
