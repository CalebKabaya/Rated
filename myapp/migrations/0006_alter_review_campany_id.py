# Generated by Django 4.0.5 on 2022-06-22 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_companies_size_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='campany_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.rating'),
        ),
    ]