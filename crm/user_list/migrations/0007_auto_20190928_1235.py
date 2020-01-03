# Generated by Django 2.2.3 on 2019-09-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0006_auto_20190928_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='booked',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='depart_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='middle_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='mobile_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='other_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='work_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='customer_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='remarks',
            field=models.TextField(null=True),
        ),
    ]