# Generated by Django 3.0.2 on 2020-01-06 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_auto_20200106_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='upload',
            field=models.FileField(blank=True, upload_to='CompletedProjects/', verbose_name='Готовый проект'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
