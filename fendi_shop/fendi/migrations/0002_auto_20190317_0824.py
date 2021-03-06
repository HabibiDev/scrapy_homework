# Generated by Django 2.1.7 on 2019-03-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fendi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_url',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='size',
            old_name='size_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='itemshop',
            name='color',
            field=models.ManyToManyField(to='fendi.Color'),
        ),
        migrations.AlterField(
            model_name='itemshop',
            name='image',
            field=models.ManyToManyField(to='fendi.Image'),
        ),
        migrations.AlterField(
            model_name='itemshop',
            name='size',
            field=models.ManyToManyField(to='fendi.Size'),
        ),
    ]
