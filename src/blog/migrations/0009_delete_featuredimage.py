# Generated by Django 4.1.7 on 2023-03-27 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_featuredimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeaturedImage',
        ),
    ]
