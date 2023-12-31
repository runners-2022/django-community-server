# Generated by Django 3.2.16 on 2023-11-08 12:33

import community.bases.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_post_profile'),
        ('comments', '0004_comment_profile'),
        ('profiles', '0001_initial'),
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Deleted')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Report User Username')),
                ('profile_image_url', models.URLField(blank=True, null=True, verbose_name='Report User Profile Image URL')),
                ('contents', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Contents')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Title')),
                ('content', models.CharField(blank=True, max_length=300, null=True, verbose_name='Content')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Report',
                'ordering': ['-created'],
            },
            bases=(community.bases.models.UpdateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ReportChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Deleted')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_data', models.JSONField(blank=True, null=True, verbose_name='User Data')),
                ('profile_data', models.JSONField(blank=True, null=True, verbose_name='Profile Data')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('content', models.CharField(blank=True, max_length=300, null=True, verbose_name='Content')),
                ('is_default', models.BooleanField(default=False, verbose_name='Is Default')),
            ],
            options={
                'verbose_name': 'Report Choice',
                'verbose_name_plural': 'Report Choice',
                'ordering': ['created'],
            },
            bases=(community.bases.models.UpdateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ReportGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Deleted')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('reported_count', models.IntegerField(default=0, verbose_name='Reported Count')),
                ('contents', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Contents')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Reported User Username')),
                ('profile_image_url', models.URLField(blank=True, null=True, verbose_name='Reported User Profile Image URL')),
                ('profile_is_banned', models.BooleanField(default=False, verbose_name='Profile Is Banned')),
                ('profile_is_deactivated', models.BooleanField(default=False, verbose_name='Profile Is Deactivated')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('is_deactivated', models.BooleanField(default=False, verbose_name='Is Deactivated')),
                ('deactivated_at', models.CharField(blank=True, max_length=100, null=True, verbose_name='Deactivated At')),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_groups', to='comments.comment', verbose_name='Comment')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_groups', to='communities.community', verbose_name='Community')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_groups', to='posts.post', verbose_name='Post')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_groups', to='profiles.profile', verbose_name='Reported User Profile')),
            ],
            options={
                'verbose_name': 'Report Group',
                'verbose_name_plural': 'Report Group',
                'ordering': ['-created'],
            },
            bases=(community.bases.models.UpdateMixin, models.Model),
        ),
    ]
