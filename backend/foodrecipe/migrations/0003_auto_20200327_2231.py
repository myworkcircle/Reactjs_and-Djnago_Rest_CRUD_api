# Generated by Django 3.0.4 on 2020-03-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodrecipe', '0002_recipe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.FileField(blank=True, upload_to='fileupload'),
        ),
    ]
