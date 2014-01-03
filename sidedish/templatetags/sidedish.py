# -*- utf-8 -*-
from django import template
from ..models import Dish
from ..utils import match_path

import re

register = template.Library()


@register.simple_tag(takes_context=True)
def sidedishes(context, side):
    request = context['request']

    dishes = []

    for dish in Dish.objects.published().filter(side=side):
        if dish.is_visible(request.path):
            dishes.append(dish)

    context['sidedishes'] = dishes
    context['side'] = side

    template_list = [
        "sidedish/%s.html" % side,
        "sidedish/side.html",
    ]

    tpl = template.loader.select_template(template_list)
    return tpl.render(template.Context(context))


@register.simple_tag(takes_context=True)
def sidedish(context, dish):
    request = context['request']

    try:
        if not isinstance(dish, Dish):
            dish = Dish.objects.published().get(slug=dish)

        if dish.is_visible(request.path):
            context['sidedish'] = dish

        template_list = [
            "sidedish/%s.html" % dish.slug,
            "sidedish/sidedish.html",
        ]
    except:
        return None

    tpl = template.loader.select_template(template_list)
    return tpl.render(template.Context(context))
