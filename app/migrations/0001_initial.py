# Generated by Django 4.2.5 on 2023-09-10 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Nothing', max_length=1000)),
                ('price', models.IntegerField(default=0)),
                ('photo', models.ImageField(upload_to='food')),
            ],
        ),
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Nothing', max_length=1000)),
                ('location', models.CharField(default='Nothing', max_length=100)),
                ('min_price', models.IntegerField(default=0)),
                ('max_price', models.IntegerField(default=0)),
                ('seats', models.IntegerField(default=0)),
                ('tables', models.IntegerField(default=0)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='restaurantcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='Nothing', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField(default=0)),
                ('booking_status', models.BooleanField(default=False)),
                ('restaurant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.restaurantcategories'),
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='nothing', max_length=1000)),
                ('photo', models.ImageField(upload_to='user')),
                ('phone', models.CharField(default='nothing', max_length=1000)),
                ('trusted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='foodorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.BooleanField(default=False)),
                ('item', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.fooditem')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.restaurant'),
        ),
        migrations.CreateModel(
            name='bookingrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.restaurant')),
                ('table', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.table')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
