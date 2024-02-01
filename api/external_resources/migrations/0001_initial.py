# Generated by Django 3.2.23 on 2024-01-31 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('features', '0062_alter_feature_segment_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('type', models.TextField()),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='FeatureExternalResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featureexternalresources', to='external_resources.externalresources')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.feature')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='externalresources',
            name='feature_external_resource',
            field=models.ManyToManyField(blank=True, through='external_resources.FeatureExternalResources', to='features.Feature'),
        ),
        migrations.AlterUniqueTogether(
            name='externalresources',
            unique_together={('url',)},
        ),
    ]
