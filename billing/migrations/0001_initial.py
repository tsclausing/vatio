# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Plan'
        db.create_table(u'billing_plan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fixed_cost', self.gf('django.db.models.fields.DecimalField')(default=25.0, max_digits=8, decimal_places=2)),
            ('user_cost', self.gf('django.db.models.fields.DecimalField')(default=2.0, max_digits=8, decimal_places=2)),
            ('max_users', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('teams', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'billing', ['Plan'])


    def backwards(self, orm):
        # Deleting model 'Plan'
        db.delete_table(u'billing_plan')


    models = {
        u'billing.plan': {
            'Meta': {'object_name': 'Plan'},
            'fixed_cost': ('django.db.models.fields.DecimalField', [], {'default': '25.0', 'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_users': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'teams': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_cost': ('django.db.models.fields.DecimalField', [], {'default': '2.0', 'max_digits': '8', 'decimal_places': '2'})
        }
    }

    complete_apps = ['billing']