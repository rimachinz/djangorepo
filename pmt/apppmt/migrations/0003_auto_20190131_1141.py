# Generated by Django 2.1.5 on 2019-01-31 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppmt', '0002_document_wiki'),
    ]

    operations = [
        migrations.DeleteModel(
            name='document',
        ),
        migrations.DeleteModel(
            name='wiki',
        ),
        migrations.AddField(
            model_name='issues',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='issues',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='project',
            name='task',
            field=models.TextField(default='SOME STRING', max_length=500),
        ),
    ]
