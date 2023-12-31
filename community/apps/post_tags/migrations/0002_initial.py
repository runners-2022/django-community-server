# Generated by Django 3.2.16 on 2023-11-08 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post_tags', '0001_initial'),
        ('posts', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttag',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='posts.post', verbose_name='Post'),
        ),
        migrations.AddField(
            model_name='posttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='tags.tag', verbose_name='Tag'),
        ),
    ]
