# Generated by Django 3.2.5 on 2022-03-31 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0003_alter_qrcode_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
