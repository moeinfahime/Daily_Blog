from django import template
from ..models import Category

register = template.Library()


@register.simple_tag
def title(data="The Daily Blog"):
    return data


@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return  {"category": Category.objects.filter(status=True)}
