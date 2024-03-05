from django.shortcuts import render
from blog.models import BlogIndexPage, BlogPage

# Create your views here.
def index_blog(request):

    page = BlogIndexPage.objects.all().order_by('-id').first()

    context = {
        'page':page
    }

    return render(
        request,
        'blog/blog_index_page.html',
        context=context
    )


def blog_page(request, id: int):
    post = BlogPage.objects.filter(id=id).first()

    context = {
        'page':post
    }

    return render(
        request,
        'blog/blog_page.html',
        context=context
    )
