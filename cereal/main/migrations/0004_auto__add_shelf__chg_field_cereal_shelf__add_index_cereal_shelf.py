# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shelf'
        db.create_table(u'main_shelf', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Shelf'])


        # Renaming column for 'Cereal.shelf' to match new field type.
        db.rename_column(u'main_cereal', 'shelf', 'shelf_id')
        # Changing field 'Cereal.shelf'
        db.alter_column(u'main_cereal', 'shelf_id', self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['main.Shelf']))
        # Adding index on 'Cereal', fields ['shelf']
        db.create_index(u'main_cereal', ['shelf_id'])


    def backwards(self, orm):
        # Removing index on 'Cereal', fields ['shelf']
        db.delete_index(u'main_cereal', ['shelf_id'])

        # Deleting model 'Shelf'
        db.delete_table(u'main_shelf')


        # Renaming column for 'Cereal.shelf' to match new field type.
        db.rename_column(u'main_cereal', 'shelf_id', 'shelf')
        # Changing field 'Cereal.shelf'
        db.alter_column(u'main_cereal', 'shelf', self.gf('django.db.models.fields.IntegerField')(null=True))

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
            'shelf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Shelf']"}),
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
        },
        u'main.shelf': {
            'Meta': {'object_name': 'Shelf'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']