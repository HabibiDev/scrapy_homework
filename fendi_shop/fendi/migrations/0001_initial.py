# Generated by Django 2.1.7 on 2019-03-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ItemShop',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=50)),
                ('color', models.ManyToManyField(
                    blank=True, null=True, to='fendi.Color')),
                ('image', models.ManyToManyField(
                    blank=True, null=True, to='fendi.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='itemshop',
            name='size',
            field=models.ManyToManyField(
                blank=True, null=True, to='fendi.Size'),
        ),
    ]
