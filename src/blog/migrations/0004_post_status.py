# Generated by Django 4.1.7 on 2023-03-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='draft', max_length=10),
        ),
    ]
