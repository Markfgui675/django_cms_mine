from django.shortcuts import render
from blog.models import BlogIndexPage

# Create your views here.
def index_blog(request):

    artigos = BlogIndexPage.objects.all().order_by('-id')

    print(artigos[0])

    context = {
        'page':artigos
    }

    return render(
        request,
        'blog/blog_index_page.html',
        context=context
    )
