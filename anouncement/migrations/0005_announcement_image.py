# Generated by Django 5.0 on 2023-12-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anouncement', '0004_alter_announcement_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='image',
            field=models.ImageField(default='https://media.istockphoto.com/id/1344512181/vector/icon-red-loudspeaker.jpg?s=612x612&w=0&k=20&c=MSi3Z2La8OYjSY-pr0bB6f33NOuUKAQ_LBUooLhLQsk=', upload_to=''),
        ),
    ]
