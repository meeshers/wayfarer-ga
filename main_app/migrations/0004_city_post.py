# Generated by Django 3.0.7 on 2020-06-19 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_city_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Post'),
        ),
    ]