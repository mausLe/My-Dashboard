# Generated by Django 3.2.dev20201005102505 on 2021-07-18 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_rename_img_watchlist_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='image',
        ),
    ]