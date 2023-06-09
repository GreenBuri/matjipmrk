# Generated by Django 4.1.7 on 2023-03-14 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("matjipmrk", "0004_delete_autocoords_filter_etc_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 3, 14, 11, 28, 8, 47589)
            ),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="foodtype",
            field=models.CharField(
                choices=[
                    ("korean", "한식"),
                    ("japanese", "일식"),
                    ("chinese", "중식"),
                    ("western", "양식"),
                    ("etc", "기타"),
                ],
                default="korean",
                max_length=20,
            ),
        ),
    ]
