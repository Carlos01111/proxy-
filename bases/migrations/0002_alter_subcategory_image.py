# Generated by Django 4.0.6 on 2022-08-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subcategory'),
        ),
    ]
