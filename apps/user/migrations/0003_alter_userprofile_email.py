# Generated by Django 5.0.6 on 2024-05-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userprofile_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='邮箱'),
        ),
    ]
