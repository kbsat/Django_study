from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
from django.conf import settings  # 해당 부분 추가!
from django.conf.urls.static import static  # 해당 부분 추가!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('account/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
