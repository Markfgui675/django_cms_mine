from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from .views import index, feedback_slug

@hooks.register('register_admin_urls')
def register_feddback_url():
    return [
        path('feedbacks/', index, name='feedbacks'),
        path('feedbacks/<slug>/', feedback_slug, name='feedbacks-slug'),
    ]

@hooks.register('register_admin_menu_item')
def register_feedback_menu_item():
    return MenuItem('Feedbacks', reverse('feedbacks'), icon_name='comment')
