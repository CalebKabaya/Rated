# Generated by Django 4.0.5 on 2022-06-22 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_blog_article_alter_review_campany_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='campany_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campany', to='myapp.companies'),
        ),
    ]