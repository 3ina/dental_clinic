# Generated by Django 4.2.4 on 2023-09-06 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0013_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonial', to='clinic.clinic'),
        ),
    ]