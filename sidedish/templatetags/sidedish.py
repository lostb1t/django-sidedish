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
        if (dish.pages == "" or not dish.pages) or match_path(request.path, dish.pages):
            dishes.append(dish)

    context['sidedishes'] = dishes
    context['side'] = side

    template_list = [
        "sidedish/%s.html" % side,
        "sidedish/side.html",
    ]

    tpl = template.loader.get_template('sidedish/side.html')
    return tpl.render(template.Context(context))


@register.simple_tag(takes_context=True)
def sidedish(context, slug):
    request = context['request']

    try:
        dish = Dish.objects.published().get(slug=slug)

        if match_path(request.path, dish.pages):
            context['dish'] = dish

        template_list = [
            "sidedish/%s.html" % dish.slug,
            "sidedish/dish.html",
        ]
    except:
        return None

    tpl = template.loader.select_template(template_list)
    return tpl.render(template.Context(context))
