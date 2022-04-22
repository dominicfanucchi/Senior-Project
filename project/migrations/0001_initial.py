# Generated by Django 4.0.1 on 2022-03-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nlp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('date_created', models.CharField(max_length=20000, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('ANALYZED', 'Analyzed')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speech_Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('speech_to_be_analyzed', models.CharField(max_length=20000, null=True)),
            ],
        ),
    ]