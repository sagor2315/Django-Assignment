# Generated by Django 4.1.7 on 2023-03-27 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_images', to='blog.post')),
            ],
        ),
    ]
