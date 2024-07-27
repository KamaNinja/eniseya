# Generated by Django 5.0.7 on 2024-07-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['service_category', 'title']},
        ),
        migrations.AlterModelManagers(
            name='employee',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
