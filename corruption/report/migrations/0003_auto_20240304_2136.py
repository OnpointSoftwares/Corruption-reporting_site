# Generated by Django 3.2.24 on 2024-03-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='item_type',
            field=models.CharField(choices=[('video', 'Video'), ('audio', 'Audio'), ('picture', 'Picture'), ('document', 'Document')], max_length=10),
        ),
    ]