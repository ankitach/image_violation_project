# Generated by Django 4.2.1 on 2023-06-01 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_violation', '0005_alter_vid_stream_cameras_camera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vid_stream_violations',
            name='viol_camera_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_violation.vid_stream_cameras'),
        ),
    ]
