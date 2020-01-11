# Generated by Django 3.0.2 on 2020-01-06 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_auto_20200104_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(blank=True, upload_to='CompletedProjects/', verbose_name='Готовый проект')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='upload',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.File'),
        ),
    ]
