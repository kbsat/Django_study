from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
from django.conf import settings # 외워야해
from django.conf.urls.static import static # 외워야해

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.index, name="index"),
    path('blog/',include('blogapp.urls')),
    path('portfolio/',portfolio.views.portfolio,name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 외워야해
# 이런식으로 적어도 됨
#  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA.OOT)