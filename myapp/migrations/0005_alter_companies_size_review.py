# Generated by Django 4.0.5 on 2022-06-22 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0004_remove_companies_camp_category_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='size',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=120)),
                ('job_title', models.EmailField(max_length=254)),
                ('pros', models.TextField(blank=True)),
                ('cons', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('work_enviroment', models.IntegerField(blank=True, choices=[(1, 'Permanent work from home'), (2, 'Working from office'), (3, 'Hybrid (working from office & home)'), (4, 'Unclear at the moment')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('campany_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.companies')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
