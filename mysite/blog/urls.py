from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index_blog, name='index-blog'),
    path('blog/<int:id>', views.blog_page, name='page-blog')
]


