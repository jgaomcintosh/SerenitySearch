# Generated by Django 3.2.16 on 2022-11-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0018_scoretable_parkcount"),
    ]

    operations = [
        migrations.AddField(
            model_name="scoretable",
            name="grade",
            field=models.CharField(default="N", max_length=10),
        ),
    ]
