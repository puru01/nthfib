# Generated by Django 2.1.7 on 2019-03-15 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("fibonacci", "0001_initial")]

    operations = [
        migrations.RenameField(
            model_name="fibresult", old_name="time", new_name="timeTaken"
        ),
        migrations.AlterField(
            model_name="fibresult", name="nthFib", field=models.IntegerField()
        ),
    ]
