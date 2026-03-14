from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # blog: главная, посты, категории
    path('', include('blog.urls', namespace='blog')),

    # pages: about, rules
    path('pages/', include('pages.urls', namespace='pages')),
]
