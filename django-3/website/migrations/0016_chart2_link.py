# Generated by Django 4.0.4 on 2022-06-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_chart2'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart2',
            name='link',
            field=models.CharField(default=1, max_length=234),
            preserve_default=False,
        ),
    ]
