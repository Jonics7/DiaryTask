# Generated by Django 3.0.2 on 2020-01-06 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_auto_20200106_0306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'Готовый проект'},
        ),
        migrations.AlterField(
            model_name='project',
            name='upload',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.File', verbose_name='Готовый проект'),
        ),
    ]
