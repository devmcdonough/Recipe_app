# Generated by Django 4.2.16 on 2024-09-20 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_picture.png', upload_to='recipes'),
        ),
    ]
