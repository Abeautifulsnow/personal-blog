from django import template

from ..models import RelatedLinks


register = template.Library()


@register.simple_tag
def display_links():
    return RelatedLinks.objects.all()
