# Generated by Django 4.0.4 on 2022-05-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_tags_alter_editor_options_editor_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='photos/default.jpg', upload_to='articles/'),
        ),
    ]
