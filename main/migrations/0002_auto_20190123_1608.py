# Generated by Django 2.1.5 on 2019-01-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='mother_tongue',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
