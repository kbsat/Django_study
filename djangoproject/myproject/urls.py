from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.home, name="home"), 
    # name을 설정하는 이유? views에서 함수명이 바뀔 경우를 대비
    # name은 대부분 views의 함수와 이름이 같게 설정!
]
