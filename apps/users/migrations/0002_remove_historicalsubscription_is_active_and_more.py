# Generated by Django 4.1 on 2022-09-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="historicalsubscription", name="is_active",),
        migrations.RemoveField(model_name="subscription", name="is_active",),
        migrations.AddField(
            model_name="historicalsubscription",
            name="count_sub_total",
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="subscription",
            name="count_sub_total",
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
