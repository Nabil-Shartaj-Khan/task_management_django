# Generated by Django 5.1.7 on 2025-03-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_secured_webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualtask',
            name='task_description',
            field=models.TextField(),
        ),
    ]
