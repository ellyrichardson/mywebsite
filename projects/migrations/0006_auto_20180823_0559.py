# Generated by Django 2.0.5 on 2018-08-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180823_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='id',
        ),
        migrations.AlterField(
            model_name='projects',
            name='feature_images',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
