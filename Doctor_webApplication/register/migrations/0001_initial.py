# Generated by Django 3.2.12 on 2022-10-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Phone_Number', models.CharField(max_length=15)),
                ('Home_Address', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=10)),
            ],
        ),
    ]