# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'entidad'
        db.create_table(u'core_entidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('father', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['entidad'])

        # Adding model 'liberar'
        db.create_table(u'core_liberar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.entidad'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('month', self.gf('django.db.models.fields.IntegerField')()),
            ('liberate', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['liberar'])

        # Adding model 'solicitud'
        db.create_table(u'core_solicitud', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.entidad'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('month', self.gf('django.db.models.fields.IntegerField')()),
            ('request', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['solicitud'])

        # Adding model 'log'
        db.create_table(u'core_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.entidad'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('month', self.gf('django.db.models.fields.IntegerField')()),
            ('liberate', self.gf('django.db.models.fields.IntegerField')()),
            ('request', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['log'])


    def backwards(self, orm):
        # Deleting model 'entidad'
        db.delete_table(u'core_entidad')

        # Deleting model 'liberar'
        db.delete_table(u'core_liberar')

        # Deleting model 'solicitud'
        db.delete_table(u'core_solicitud')

        # Deleting model 'log'
        db.delete_table(u'core_log')


    models = {
        u'core.entidad': {
            'Meta': {'object_name': 'entidad'},
            'father': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.liberar': {
            'Meta': {'object_name': 'liberar'},
            'entidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.entidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liberate': ('django.db.models.fields.IntegerField', [], {}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.log': {
            'Meta': {'object_name': 'log'},
            'entidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.entidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liberate': ('django.db.models.fields.IntegerField', [], {}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'request': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.solicitud': {
            'Meta': {'object_name': 'solicitud'},
            'entidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.entidad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'request': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']