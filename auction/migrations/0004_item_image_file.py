# Generated by Django 4.2.14 on 2025-02-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_alter_item_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_file',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
