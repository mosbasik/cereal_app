# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Kind'
        db.delete_table(u'main_kind')

        # Deleting model 'Manufacturer'
        db.delete_table(u'main_manufacturer')

        # Deleting field 'Cereal.kind'
        db.delete_column(u'main_cereal', 'kind_id')

        # Deleting field 'Cereal.manufacturer'
        db.delete_column(u'main_cereal', 'manufacturer_id')


    def backwards(self, orm):
        # Adding model 'Kind'
        db.create_table(u'main_kind', (
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Kind'])

        # Adding model 'Manufacturer'
        db.create_table(u'main_manufacturer', (
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Manufacturer'])

        # Adding field 'Cereal.kind'
        db.add_column(u'main_cereal', 'kind',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['main.Kind']),
                      keep_default=False)

        # Adding field 'Cereal.manufacturer'
        db.add_column(u'main_cereal', 'manufacturer',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['main.Manufacturer']),
                      keep_default=False)


    models = {
        u'main.cereal': {
            'Meta': {'object_name': 'Cereal'},
            'calorie': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'carb': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cup': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fiber': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'potassium': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'protein': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shelf': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sodium': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sugar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vitamin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']