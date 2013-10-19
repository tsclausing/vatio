# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'account_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('org', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['organization.Organization'], unique=True, null=True)),
            ('is_org_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_org_delegate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_dept_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('timezone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'account', ['Profile'])

        # Adding M2M table for field dept on 'Profile'
        m2m_table_name = db.shorten_name(u'account_profile_dept')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm[u'account.profile'], null=False)),
            ('department', models.ForeignKey(orm[u'organization.department'], null=False))
        ))
        db.create_unique(m2m_table_name, ['profile_id', 'department_id'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'account_profile')

        # Removing M2M table for field dept on 'Profile'
        db.delete_table(db.shorten_name(u'account_profile_dept'))


    models = {
        u'account.profile': {
            'Meta': {'object_name': 'Profile'},
            'dept': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'profile+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['organization.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_dept_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_org_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_org_delegate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'org': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['organization.Organization']", 'unique': 'True', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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

    complete_apps = ['account']