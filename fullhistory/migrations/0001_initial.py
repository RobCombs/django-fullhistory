# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Request'
        db.create_table('fullhistory_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('user_pk', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, db_index=True)),
            ('request_path', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('fullhistory', ['Request'])

        # Adding model 'FullHistory'
        db.create_table('fullhistory_fullhistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('revision', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('action_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('_data', self.gf('django.db.models.fields.TextField')(db_column='data')),
            ('request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fullhistory.Request'], null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('info', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('fullhistory', ['FullHistory'])

        # Adding unique constraint on 'FullHistory', fields ['revision', 'content_type', 'object_id']
        db.create_unique('fullhistory_fullhistory', ['revision', 'content_type_id', 'object_id'])


    def backwards(self, orm):

        # Deleting model 'Request'
        db.delete_table('fullhistory_request')

        # Deleting model 'FullHistory'
        db.delete_table('fullhistory_fullhistory')

        # Removing unique constraint on 'FullHistory', fields ['revision', 'content_type', 'object_id']
        db.delete_unique('fullhistory_fullhistory', ['revision', 'content_type_id', 'object_id'])


    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fullhistory.fullhistory': {
            'Meta': {'unique_together': "(('revision', 'content_type', 'object_id'),)", 'object_name': 'FullHistory'},
            '_data': ('django.db.models.fields.TextField', [], {'db_column': "'data'"}),
            'action': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fullhistory.Request']", 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"})
        },
        'fullhistory.request': {
            'Meta': {'object_name': 'Request'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user_pk': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'db_index': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'media_type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'music_format': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site_type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fullhistory']
