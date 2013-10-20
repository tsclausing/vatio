# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Department.org'
        db.alter_column(u'organization_department', 'org_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['organization.Organization'], unique=True, null=True))

    def backwards(self, orm):

        # Changing field 'Department.org'
        db.alter_column(u'organization_department', 'org_id', self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['organization.Organization'], unique=True))

    models = {
        u'organization.department': {
            'Meta': {'object_name': 'Department'},
            'dept': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organization.Department']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'org': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['organization.Organization']", 'unique': 'True', 'null': 'True'})
        },
        u'organization.organization': {
            'Meta': {'object_name': 'Organization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['organization']