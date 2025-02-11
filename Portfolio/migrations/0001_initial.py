# Generated by Django 5.1.4 on 2025-01-14 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('intro', models.TextField()),
                ('project_description', models.TextField()),
                ('category_type', models.CharField(choices=[('web', 'Web Development'), ('desktop', 'Desktop Application'), ('data', 'Data Science'), ('app', 'Mobile App')], max_length=50)),
                ('stack', models.TextField()),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('pending', 'Pending')], max_length=20)),
                ('images', models.ImageField(blank=True, null=True, upload_to='projects/')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project/images/', verbose_name='Image')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_images', to='Portfolio.project')),
            ],
        ),
    ]
