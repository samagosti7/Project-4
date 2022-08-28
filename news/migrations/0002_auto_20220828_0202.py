# Generated by Django 3.2.15 on 2022-08-28 02:02
"""
        This file migrates the changes to the models regarding status,
        and ability to be commented on.
    """

from django.db import migrations, models


class Migration(migrations.Migration):
    """
        This describes the second migration
    """

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')],
                                      default=1),
        ),
    ]
