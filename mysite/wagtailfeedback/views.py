from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import BlogPage
from datetime import date
from django.utils.timezone import now, datetime
from wagtailfeedback.forms.create_feedback import FeedbackcreateForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(
        request, 'wagtailfeedback/index.html'
    )

def feedback(request, slug):
    page = BlogPage.objects.filter(slug=slug).first()
    feedback_form_data = request.session.get('feedback_form_data', None)
    form = FeedbackcreateForm(feedback_form_data)
    context = {
        'slug':slug,
        'page':page,
        'form':form,
        'form_action':reverse('feedback-create', args=(slug,))
    }
    if request:
        return render(request, 'wagtailfeedback/feedback.html', context=context)


def feedback_create(request, slug):
    print(f'aqui ó: {slug}')
    print(date.today())
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['feedback_form_data'] = POST
    form = FeedbackcreateForm(POST)

    if form.is_valid():
        messages.success(request, 'Feedback')
        feedback = form.save(commit=False)
        feedback.slug(slug)
        feedback.save()
        del(request.session['feedback_form_data'])
    
    return redirect(feedback_success)

def feedback_success(request):
    return HttpResponse('Deu certo')
