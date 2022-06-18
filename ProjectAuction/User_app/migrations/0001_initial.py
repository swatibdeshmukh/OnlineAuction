# Generated by Django 4.0.5 on 2022-06-18 10:51

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('area_id', models.IntegerField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=200)),
                ('street_name', models.CharField(max_length=150)),
                ('house_no', models.CharField(max_length=50)),
                ('area_pincode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=50)),
                ('country_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.country')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.BigIntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.address')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='IdProof',
            fields=[
                ('idproof_id', models.IntegerField(primary_key=True, serialize=False)),
                ('idproof_type', models.CharField(max_length=50)),
                ('idproof_image', models.ImageField(upload_to='idphoto/')),
                ('myuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.state')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.city'),
        ),
    ]
