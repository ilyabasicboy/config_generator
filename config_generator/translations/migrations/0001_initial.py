# Generated by Django 2.2.28 on 2022-10-12 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configurator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='name of language')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Key')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translations.Language', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Translation key',
                'verbose_name_plural': 'Translation keys',
                'unique_together': {('language', 'title')},
            },
        ),
        migrations.CreateModel(
            name='ImportTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translations.Language', verbose_name='language')),
            ],
            options={
                'verbose_name': 'Import translation',
                'verbose_name_plural': 'Import translation',
            },
        ),
        migrations.CreateModel(
            name='CustomTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.WhiteLabelConfig')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translations.Key', verbose_name='key')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translations.Language', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Custom translation',
                'verbose_name_plural': 'Custom translations',
                'unique_together': {('language', 'key', 'config')},
            },
        ),
    ]
