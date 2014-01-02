# -*- utf-8 -*-
from django import template
from ..models import Dish
from ..utils import match_path

import re

register = template.Library()


@register.simple_tag(takes_context=True)
def sidedish_side(context, side):
    request = context['request']

    pks = []
    dishes = None

    for dish in Dish.objects.published().filter(side=side):
        if match_path(request.path, dish.pages):
            pks += [dish.pk]

    if len(pks) != 0:
        dish = Dish.objects.published().filter(pk__in=pks)

    context['dishes'] = dishes
    context['side'] = side

    tpl = template.loader.get_template('sidedish/side.html')
    return tpl.render(template.Context(context))


@register.simple_tag(takes_context=True)
def sidedish_dish(context, slug):
    request = context['request']

    try:
        dish = Dish.objects.published().get(slug=slug)

        if match_path(request.path, dish.pages):
            context['dish'] = dish
    except:
        context['dish'] = None

    tpl = template.loader.get_template('sidedish/dish.html')
    return tpl.render(template.Context(context))
