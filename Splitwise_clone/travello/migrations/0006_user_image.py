# Generated by Django 2.2.6 on 2019-11-23 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_group_member_group_membership_group_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myid', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
            ],
        ),
    ]
