# Generated by Django 2.1.1 on 2019-09-28 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0004_auto_20190924_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recent_SW_notie', models.CharField(max_length=120)),
            ],
        ),
    ]
