# Generated by Django 3.2.6 on 2022-05-04 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_alter_recipe_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageContents',
            fields=[
                ('page_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('owners', models.TextField(null=True)),
                ('status', models.TextField(null=True)),
            ],
        ),
    ]
