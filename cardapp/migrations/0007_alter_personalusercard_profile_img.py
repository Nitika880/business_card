# Generated by Django 3.2.5 on 2022-04-01 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0006_qrcode_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalusercard',
            name='profile_img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
