from django import template

register = template.Library()


@register.simple_tag
def get_search_item(request):
    pass
