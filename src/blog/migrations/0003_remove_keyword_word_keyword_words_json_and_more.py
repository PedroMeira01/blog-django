# Generated by Django 4.2.5 on 2023-09-13 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_keyword_post_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='word',
        ),
        migrations.AddField(
            model_name='keyword',
            name='words_json',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='post',
            name='keywords',
        ),
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.keyword'),
        ),
    ]