from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:blog_id>',views.detail,name="detail"),
    path('new/',views.new,name = "new"),
    path('create/',views.create,name="create"),
    path('delete/<int:blog_id>',views.delete,name="delete"),
]