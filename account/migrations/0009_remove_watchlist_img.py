# Generated by Django 3.2.dev20201005102505 on 2021-07-17 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_watchlist_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='img',
        ),
    ]