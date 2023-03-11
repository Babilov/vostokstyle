from django import template
from main.models import AllItems

register = template.Library()


@register.simple_tag
def get_description_by_id(pk):
    # print(AllItems.objects.get(pk=pk).description)
    return AllItems.objects.get(pk=pk).description
