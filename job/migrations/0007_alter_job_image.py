# Generated by Django 3.2.9 on 2021-11-11 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='job/'),
        ),
    ]
