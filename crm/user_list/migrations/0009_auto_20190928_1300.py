# Generated by Django 2.2.3 on 2019-09-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0008_auto_20190928_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='booked',
            field=models.IntegerField(default=1),
        ),
    ]
