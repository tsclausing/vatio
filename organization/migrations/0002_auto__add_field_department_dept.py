# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Department.dept'
        db.add_column(u'organization_department', 'dept',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organization.Department'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field dept on 'Department'
        db.delete_table(db.shorten_name(u'organization_department_dept'))


    def backwards(self, orm):
        # Deleting field 'Department.dept'
        db.delete_column(u'organization_department', 'dept_id')

        # Adding M2M table for field dept on 'Department'
        m2m_table_name = db.shorten_name(u'organization_department_dept')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('department', models.ForeignKey(orm[u'organization.department'], null=False)),
            ('organization', models.ForeignKey(orm[u'organization.organization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['department_id', 'organization_id'])


    models = {
        u'organization.department': {
            'Meta': {'object_name': 'Department'},
            'dept': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organization.Department']", 'null': 'True', 'blank': 'True'}),
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