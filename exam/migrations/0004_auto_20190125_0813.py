# Generated by Django 2.1.5 on 2019-01-25 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20190125_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marksentry',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.ExamSchedule'),
        ),
    ]