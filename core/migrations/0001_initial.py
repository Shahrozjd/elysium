# Generated by Django 4.0.4 on 2022-07-04 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.PositiveIntegerField(blank=True, default=0)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=225)),
                ('last_name', models.CharField(blank=True, max_length=225)),
                ('company_name', models.CharField(blank=True, max_length=225)),
                ('Country', models.CharField(blank=True, max_length=225)),
                ('street_address', models.TextField(blank=True, max_length=500)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('state', models.CharField(blank=True, max_length=255)),
                ('Post_code', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=11, unique=True)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('occupation', models.CharField(blank=True, max_length=225)),
                ('gender', models.CharField(blank=True, max_length=225)),
                ('father_name', models.CharField(blank=True, max_length=225)),
                ('blood_group', models.CharField(blank=True, max_length=25)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('religion', models.CharField(blank=True, max_length=25)),
                ('nationality', models.CharField(blank=True, max_length=25)),
                ('hobby', models.CharField(blank=True, max_length=225)),
                ('source', models.CharField(choices=[('fitness', 'fitness'), ('reduce_weight', 'Reduce Weight'), ('increase_weight', 'Increase Weight'), ('hyper_trophy', 'Hyper Trophy')], default='fitness', max_length=225)),
                ('approved', models.BooleanField(default=False)),
                ('dues_paid', models.BooleanField(default=False)),
                ('membership_updated_on', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Membership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.membership')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_time', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
    ]