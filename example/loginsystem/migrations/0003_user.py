# Generated by Django 4.2.7 on 2023-11-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsystem', '0002_rename_cofirm_usersignup_pass2'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('pass1', models.CharField(max_length=50)),
                ('pass2', models.CharField(max_length=50)),
            ],
        ),
    ]