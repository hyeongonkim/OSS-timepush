# Generated by Django 2.1.1 on 2019-09-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0007_recentkmtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='kmtitle',
            name='km_link',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='kmtitle',
            name='km_title',
            field=models.CharField(max_length=200),
        ),
    ]
