# Generated by Django 4.0.5 on 2022-06-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
