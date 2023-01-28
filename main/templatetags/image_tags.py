from django import template
from main.models import Images

register = template.Library()


@register.simple_tag
def get_image_by_item_id(item_id):
    return Images.objects.filter(item_id=item_id)


@register.simple_tag
def get_main_image_by_id(item_id):
    return Images.objects.filter(item_id=item_id, main_photo=True)[0]

