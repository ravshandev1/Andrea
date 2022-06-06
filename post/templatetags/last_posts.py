from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def last_posts():
    try:
        posts = Post.objects.order_by('-id')[:3]
    except:
        posts = None
    return posts


@register.simple_tag()
def tags():
    try:
        tag = Tag.objects.all()
    except:
        tag = None
    return tag


@register.simple_tag()
def categories():
    try:
        category = Category.objects.all()
    except:
        category = None
    return category
