# Generated by Django 3.2.5 on 2022-04-01 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0004_alter_qrcode_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalusercard',
            name='multi_images',
        ),
    ]
