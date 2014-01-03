from datetime import datetime

from django.db.models import Manager, Q, TextField, get_models
from django.db.models.query import QuerySet
from django.contrib.sites.managers import CurrentSiteManager
from django.utils.encoding import force_unicode

from . import settings


class PublishedMixin(object):
    def published(self):
        return self.filter(
            Q(publish_date__lte=datetime.now) | Q(publish_date__isnull=True),
            Q(expiry_date__gte=datetime.now) | Q(expiry_date__isnull=True),
            Q(status=settings.SIDEDISH_STATUS_PUBLISHED))


class PublishedQuerySet(QuerySet, PublishedMixin):
    pass


class PublishedManager(Manager, PublishedMixin):
    def get_query_set(self):
        return PublishedQuerySet(self.model, using=self._db)
