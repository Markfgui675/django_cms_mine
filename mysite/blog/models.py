from django.db import models
# Create your models here.
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    def get_context(self, request, *args, **kwargs):
        return super().get_context(request, *args, **kwargs)

class Feedback(models.Model):
    date = models.DateField('Data')
    title = models.CharField('Título', max_length=150)
    texto = models.TextField('Descrição')
    slug = models.CharField('Slug', max_length=250)

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.title
