# Generated by Django 4.2.14 on 2024-07-14 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimage',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='cars'),
        ),
    ]