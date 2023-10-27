# Generated by Django 4.2.6 on 2023-10-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rprofile', '0004_alter_userprofile_handphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='handphone',
            field=models.IntegerField(blank=True, default=1234567890, null=True),
        ),
    ]