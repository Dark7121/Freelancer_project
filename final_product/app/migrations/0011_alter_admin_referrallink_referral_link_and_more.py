# Generated by Django 5.1.2 on 2024-11-24 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_admin_referrallink_referral_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_referrallink',
            name='referral_link',
            field=models.CharField(default='7a92d4cae9cb450292642f7bd80935e7', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='staticfiles/blog_images/'),
        ),
    ]
