# Generated by Django 2.2.1 on 2019-09-24 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notice', '0003_auto_20190923_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytag',
            name='emailAccount',
        ),
        migrations.AddField(
            model_name='mytag',
            name='account',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='EmailAccount',
        ),
    ]