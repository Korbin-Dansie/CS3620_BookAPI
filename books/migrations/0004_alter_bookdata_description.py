# Generated by Django 4.2.5 on 2023-10-24 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_book_data_bookdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='description',
            field=models.TextField(max_length=1024),
        ),
    ]
