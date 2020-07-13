from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def index(request):
    blogs = Blog.objects
    return render(request,'index.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk = blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def new(request): # new.html을 띄어주는 함수
    return render(request,'new.html')

def create(request): #입력받은내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # 삭제 = blog.delete()
    return redirect('/detail/'+str(blog.id)) # 위 함수를 다 처리한 후 인자로 받은 URL로 이동
# redirect와 render의 차이 ?
# 비슷하긴 하지만 redirect함수는 안에 URL을 받기 때문에 다른 URL을 입력가능 ( ex : https://google.com )
# render함수는 세번째 인자로 딕셔너리를 담아보낼 수 있기 때문에 데이터를 처리할 때 사용