# Generated by Django 4.0 on 2022-01-08 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_id_admin_user_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='birthday',
            new_name='birthdate',
        ),
    ]
