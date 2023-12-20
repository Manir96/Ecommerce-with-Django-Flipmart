# Generated by Django 4.2.6 on 2023-10-26 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top_Banner_Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('top_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('new_collection', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('slider', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.DeleteModel(
            name='Banner_Images',
        ),
    ]
