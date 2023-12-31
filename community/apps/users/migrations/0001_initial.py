# Generated by Django 3.2.16 on 2023-11-08 12:33

import community.apps.users.models.fields.phone_number
import community.apps.users.models.managers.objects
import community.apps.users.models.mixins.image
import community.bases.models
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Deleted')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('post_bookmark_count', models.IntegerField(default=0, verbose_name='Post Bookmark Count')),
                ('comment_count', models.IntegerField(default=0, verbose_name='Comment Count')),
                ('friend_count', models.IntegerField(default=0, verbose_name='Friend Count')),
                ('profile_image_url', models.URLField(default=community.apps.users.models.mixins.image.default_profile_image_path, verbose_name='Profile Image URL')),
                ('banner_image_url', models.URLField(blank=True, null=True, verbose_name='Banner Image URL')),
                ('community_point', models.IntegerField(default=0, verbose_name='Club Point')),
                ('post_count', models.IntegerField(default=0, verbose_name='Post Count')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nickname')),
                ('phone', community.apps.users.models.fields.phone_number.CustomPhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Phone')),
                ('level', models.IntegerField(default=1, verbose_name='Level')),
                ('grade_title', models.CharField(default='NOVICE', max_length=100, verbose_name='Grade Title')),
                ('ring_color', models.CharField(default='LITE_GREY', max_length=100, verbose_name='Ring Color')),
                ('badge_image_url', models.URLField(blank=True, null=True, verbose_name='Badge Image URL')),
                ('web_url', models.URLField(blank=True, null=True, verbose_name='Web URL')),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVE', 'DEACTIVE'), ('WITHDRAWING', 'WITHDRAWING'), ('WITHDRAWN', 'WITHDRAWN')], default='ACTIVE', max_length=20, verbose_name='Status')),
                ('hash', models.CharField(blank=True, max_length=10, null=True, verbose_name='Hash')),
                ('wallet_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Wallet Address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
                'ordering': ['-created'],
            },
            bases=(community.bases.models.UpdateMixin, models.Model),
            managers=[
                ('objects', community.apps.users.models.managers.objects.UserMainManager()),
            ],
        ),
    ]
