# Generated by Django 4.1.6 on 2023-02-02 09:30

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(max_length=250, unique=True)),
                ('city', models.CharField(max_length=250, unique=True)),
                ('state', models.CharField(max_length=250, unique=True)),
                ('county', models.CharField(max_length=250, unique=True)),
                ('vat_rate', models.DecimalField(decimal_places=10, max_digits=250)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=1000)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', core.models.UpdatedUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250, unique=True)),
                ('retail_value', models.DecimalField(decimal_places=10, max_digits=250)),
                ('screen_costs', models.DecimalField(decimal_places=10, max_digits=250)),
                ('battery_costs', models.DecimalField(decimal_places=10, max_digits=250)),
                ('battery_labor_costs', models.DecimalField(decimal_places=10, max_digits=250)),
                ('memory_premium', models.DecimalField(decimal_places=10, max_digits=250)),
                ('face_ID_Bdisc', models.DecimalField(decimal_places=10, max_digits=250)),
                ('touch_ID_Bdisc', models.DecimalField(decimal_places=10, max_digits=250)),
                ('backcam_Bdisc', models.DecimalField(decimal_places=10, max_digits=250)),
                ('margin', models.CharField(max_length=250, unique=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]