# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import settings

from datetime import datetime

try:
    from ckeditor.fields import RichTextField
    TextField = RichTextField
except:
    TextField = models.TextField


class Dish(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    show_title = models.BooleanField(verbose_name=_('Show title'), default=True)
    slug = models.SlugField(max_length=128, blank=False, unique=True, help_text=_('Unique identifier for this block'))
    status = models.IntegerField(_("Status"), choices=settings.SIDEDISH_STATUS_CHOICES, default=settings.SIDEDISH_STATUS_PUBLISHED)
    publish_date = models.DateTimeField(_("Published from"), help_text=_("With published checked, won't be shown until this time"), default=datetime.now)
    expiry_date = models.DateTimeField(_("Expires on"), help_text=_("With published checked, won't be shown after this time"), blank=True, null=True)
    content = TextField(verbose_name=_('Content'), blank=True, null=True)
    side = models.CharField(verbose_name=_('Area'), max_length=20, null=True, blank=True, choices=settings.SIDEDISH_SIDES)
    pages = models.TextField(_('Pages'), blank=True, null=True, help_text=_('Enter one page per line as paths. The \'*\' character is a wildcard. Example paths: \'article\' for the article page. \'article/*\' for every article page. Use \'<front>\' for the frontpage.'))
    weight = models.PositiveSmallIntegerField(verbose_name=_('Weight'), help_text=_('Weight for block ordering'), default=500)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['weight', '-created_at']
        verbose_name = _('Dish')
        verbose_name_plural = _('Dishes')

