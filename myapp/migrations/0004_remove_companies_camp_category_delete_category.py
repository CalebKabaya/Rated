# Generated by Django 4.0.5 on 2022-06-21 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_companies_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='camp_category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]