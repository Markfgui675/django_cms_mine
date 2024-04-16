from django.shortcuts import render
import calendar
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

def index(request):
    current_year = timezone.now().year
    calendar_html = calendar.HTMLCalendar().formatyear(current_year)
    context = {
        'current_year':current_year,
        'calendar_html':calendar_html
    }
    return render(
        request, 'wagtailcalendar/index.html', context=context
    )

def month(request):
    current_year = timezone.now().year
    current_month = timezone.now().month
    calendar_html = calendar.HTMLCalendar().formatmonth(current_year, current_month)
    context = {
        'current_year':current_year,
        'calendar_html':calendar_html
    }
    return render(request,
        'wagtailcalendar/index.html', context=context
    )
