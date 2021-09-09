# Generated by Django 3.2.6 on 2021-09-09 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/', verbose_name='Thumbnail'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Video Title'),
        ),
        migrations.AlterField(
            model_name='video',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='video',
            name='upload',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='File'),
        ),
    ]
