# Generated by Django 2.0.5 on 2018-06-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20180626_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='treasure_images'),
        ),
    ]
