# Generated by Django 3.2.16 on 2023-11-08 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boards', '0001_initial'),
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgroup',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_groups', to='communities.community', verbose_name='Club'),
        ),
        migrations.AddField(
            model_name='board',
            name='board_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='boards', to='boards.boardgroup', verbose_name='Board Group'),
        ),
        migrations.AddField(
            model_name='board',
            name='community',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='communities.community', verbose_name='Community'),
        ),
    ]
