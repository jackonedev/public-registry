# Generated by Django 4.1.3 on 2022-11-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_person_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=models.ImageField(blank=True, upload_to='person/picture'),
        ),
    ]
