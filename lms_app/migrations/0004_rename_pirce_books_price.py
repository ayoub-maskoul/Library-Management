# Generated by Django 4.1.4 on 2023-03-14 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_rename_total_rentat_books_total_rented_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='pirce',
            new_name='price',
        ),
    ]
