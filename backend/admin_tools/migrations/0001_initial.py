# Generated by Django 3.2.24 on 2024-03-15 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_reported_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]