# Generated by Django 3.0.2 on 2020-04-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_review_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='...', max_length=5000)),
                ('image', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]
