# Generated by Django 5.0.3 on 2024-03-04 11:24

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
