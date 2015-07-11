# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cereal'
        db.create_table(u'main_cereal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Manufacturer'])),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Kind'])),
            ('calorie', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('protein', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fat', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sodium', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fiber', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('carb', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('sugar', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('potassium', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('vitamin', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('shelf', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cup', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Cereal'])

        # Adding model 'Manufacturer'
        db.create_table(u'main_manufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Manufacturer'])

        # Adding model 'Kind'
        db.create_table(u'main_kind', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Kind'])


    def backwards(self, orm):
        # Deleting model 'Cereal'
        db.delete_table(u'main_cereal')

        # Deleting model 'Manufacturer'
        db.delete_table(u'main_manufacturer')

        # Deleting model 'Kind'
        db.delete_table(u'main_kind')


    models = {
        u'main.cereal': {
            'Meta': {'object_name': 'Cereal'},
            'calorie': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'carb': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cup': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fiber': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Kind']"}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Manufacturer']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'potassium': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'protein': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shelf': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sodium': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sugar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vitamin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'main.kind': {
            'Meta': {'object_name': 'Kind'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'main.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']