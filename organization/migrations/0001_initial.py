# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table(u'organization_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'organization', ['Organization'])

        # Adding model 'Department'
        db.create_table(u'organization_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('org', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['organization.Organization'], unique=True)),
        ))
        db.send_create_signal(u'organization', ['Department'])

        # Adding M2M table for field dept on 'Department'
        m2m_table_name = db.shorten_name(u'organization_department_dept')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('department', models.ForeignKey(orm[u'organization.department'], null=False)),
            ('organization', models.ForeignKey(orm[u'organization.organization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['department_id', 'organization_id'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table(u'organization_organization')

        # Deleting model 'Department'
        db.delete_table(u'organization_department')

        # Removing M2M table for field dept on 'Department'
        db.delete_table(db.shorten_name(u'organization_department_dept'))


    models = {
        u'organization.department': {
            'Meta': {'object_name': 'Department'},
            'dept': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'parent+'", 'null': 'True', 'to': u"orm['organization.Organization']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'org': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['organization.Organization']", 'unique': 'True'})
        },
        u'organization.organization': {
            'Meta': {'object_name': 'Organization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['organization']