from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import BlogPage, Feedback
from wagtailfeedback.forms.create_feedback import FeedbackcreateForm
from django.contrib import messages

# Create your views here.
def index(request):

    f = Feedback.objects.all().order_by('-id')
    context = {
        'f':f
    }

    return render(
        request, 'wagtailfeedback/index.html', context=context
    )


def feedback_slug(request, slug):

    f = Feedback.objects.filter(slug=slug).first()
    p = BlogPage.objects.filter(slug=slug).first()
    context = {
        'f':f,
        'id':p.id,
    }
    return render(
        request, 'wagtailfeedback/feedback_slug.html', context=context
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
    return render(request, 'wagtailfeedback/feedback.html', context=context)


def feedback_create(request, slug):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['feedback_form_data'] = POST
    form = FeedbackcreateForm(POST)

    if form.is_valid():
        messages.success(request, 'Feedback')
        form.save()
        del(request.session['feedback_form_data'])
    
    return redirect('feedback-page', slug)
