# Generated by Django 2.1.4 on 2018-12-21 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_remove_album_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
