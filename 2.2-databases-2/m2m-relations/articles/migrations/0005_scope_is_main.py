# Generated by Django 4.0.3 on 2022-03-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_scope_article_scopes_scope_article_scope_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=None),
        ),
    ]