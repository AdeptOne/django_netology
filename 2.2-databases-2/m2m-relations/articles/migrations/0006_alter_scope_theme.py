# Generated by Django 4.0.3 on 2022-03-24 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_scope_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme', to='articles.theme'),
        ),
    ]
