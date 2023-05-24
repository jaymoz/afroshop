from django import template
from django.db.models import Avg
from ..models import Review

register = template.Library()

@register.simple_tag
def get_average_rating(item_id):
    average_rating = Review.objects.filter(item_id=item_id).aggregate(Avg('rating'))['rating__avg']
    return average_rating
