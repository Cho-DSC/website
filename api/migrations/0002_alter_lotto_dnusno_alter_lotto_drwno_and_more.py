# Generated by Django 4.0.3 on 2022-06-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotto',
            name='dnusNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lotto',
            name='drwNo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lotto',
            name='drwtNo1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lotto',
            name='drwtNo2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lotto',
            name='drwtNo3',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lotto',
            name='drwtNo4',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lotto',
            name='drwtNo5',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lotto',
            name='drwtNo6',
            field=models.IntegerField(),
        ),
    ]