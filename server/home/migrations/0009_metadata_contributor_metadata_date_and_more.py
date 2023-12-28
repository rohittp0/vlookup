# Generated by Django 4.2.7 on 2023-12-28 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_organization_remove_metadata_organization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='contributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contributions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='metadata',
            name='date',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='metadata',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='records', to='home.organization'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='metadata',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='verifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
