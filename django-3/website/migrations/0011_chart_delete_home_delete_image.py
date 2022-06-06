# Generated by Django 4.0.4 on 2022-06-03 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_delete_imag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField(default=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
