# Generated by Django 2.2.8 on 2020-02-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_api', '0005_collectionimport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namespace',
            name='avatar_url',
            field=models.URLField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='namespacelink',
            name='url',
            field=models.URLField(max_length=256),
        ),
    ]
