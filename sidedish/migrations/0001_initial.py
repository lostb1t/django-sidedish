# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dish'
        db.create_table(u'sidedish_dish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('show_title', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=128)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('side', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('pages', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=500)),
        ))
        db.send_create_signal(u'sidedish', ['Dish'])


    def backwards(self, orm):
        # Deleting model 'Dish'
        db.delete_table(u'sidedish_dish')


    models = {
        u'sidedish.dish': {
            'Meta': {'ordering': "['weight', '-created_at']", 'object_name': 'Dish'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '500'})
        }
    }

    complete_apps = ['sidedish']