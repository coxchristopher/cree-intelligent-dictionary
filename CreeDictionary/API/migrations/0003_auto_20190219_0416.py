# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-19 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_definition_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inflection',
            name='inflectionForms',
        ),
        migrations.RemoveField(
            model_name='lemma',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='lemma',
            name='inflections',
        ),
        migrations.RemoveField(
            model_name='word',
            name='definitions',
        ),
        migrations.AddField(
            model_name='attribute',
            name='fk_lemma',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='API.Lemma'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='definition',
            name='fk_word',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='API.Word'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inflection',
            name='fk_lemma',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='API.Lemma'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inflectionform',
            name='fk_inflection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='API.Inflection'),
            preserve_default=False,
        ),
    ]