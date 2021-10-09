# Generated by Django 3.2 on 2021-10-09 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('Pname', models.CharField(max_length=512, primary_key=True, serialize=False, unique=True)),
                ('price', models.FloatField(max_length=256)),
                ('brand', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=1024)),
                ('star_rating', models.FloatField(default=0.0, max_length=128)),
                ('date', models.DateTimeField(auto_now=True)),
                ('Photo', models.ImageField(default='NoImage.jpg', height_field=200, upload_to='', width_field=200)),
            ],
        ),
        migrations.CreateModel(
            name='commentP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('star_rating', models.FloatField(max_length=128)),
                ('content', models.TextField(max_length=512)),
                ('country', models.CharField(max_length=128)),
                ('Pname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yishi.products')),
            ],
        ),
    ]
