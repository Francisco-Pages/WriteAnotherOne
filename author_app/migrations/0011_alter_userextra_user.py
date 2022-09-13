# Generated by Django 4.0.3 on 2022-09-06 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('author_app', '0010_alter_userextra_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextra',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
