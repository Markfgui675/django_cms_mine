from django.shortcuts import render
from home.models import HomePage

def home(request):
    home = HomePage.objects.all().order_by('id').first()

    context = {
        'page':home
    }
    
    return render(
        request,
        'home/home_page.html',
        context=context
    )
