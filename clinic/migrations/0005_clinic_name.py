# Generated by Django 4.2.4 on 2023-09-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_alter_clinic_facebook_alter_clinic_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]