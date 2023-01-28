from django import template
from main.models import AllItems

register = template.Library()


@register.simple_tag
def get_price(pk):
    return AllItems.objects.get(pk=pk).price


@register.simple_tag
def get_name(pk):
    return AllItems.objects.get(pk=pk).name

