# Generated by Django 3.2 on 2021-11-15 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yishi', '0008_advice'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supermarket', models.CharField(blank=True, max_length=128)),
                ('position', models.CharField(blank=True, max_length=128)),
                ('time', models.DateField(blank=True)),
                ('postcode', models.CharField(blank=True, max_length=128)),
                ('describsion', models.TextField(max_length=512)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='commentB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=512)),
                ('Bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yishi.buyinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'commentPs',
            },
        ),
    ]
