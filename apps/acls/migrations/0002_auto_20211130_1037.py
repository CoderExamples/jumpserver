# Generated by Django 3.1.13 on 2021-11-30 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loginacl',
            options={'ordering': ('priority', '-date_updated', 'name'), 'verbose_name': 'Login acl'},
        ),
        migrations.AlterModelOptions(
            name='loginassetacl',
            options={'ordering': ('priority', '-date_updated', 'name'), 'verbose_name': 'Login asset acl'},
        ),
    ]