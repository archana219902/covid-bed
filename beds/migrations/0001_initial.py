# Generated by Django 3.2.1 on 2021-05-05 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('district', models.CharField(choices=[('AL', 'Alappuzha'), ('ER', 'Ernakulam'), ('ID', 'Idukki'), ('KN', 'Kannur'), ('KS', 'Kasaragod'), ('KL', 'Kollam'), ('KT', 'Kottayam'), ('KZ', 'Kozhikode'), ('MA', 'Malappuram'), ('PL', 'Palakkad'), ('PT', 'Pathanamthitta'), ('TV', 'Thiruvananthapuram'), ('TS', 'Thrissur'), ('WA', 'Wayanad')], max_length=2)),
                ('phone', models.IntegerField()),
                ('sector', models.CharField(choices=[('gov', 'Government'), ('prv', 'Private')], max_length=3)),
                ('covid_beds', models.IntegerField()),
                ('normal_beds', models.IntegerField()),
                ('icu_beds', models.IntegerField()),
                ('ventilator', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('aadharno', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('district', models.CharField(choices=[('AL', 'Alappuzha'), ('ER', 'Ernakulam'), ('ID', 'Idukki'), ('KN', 'Kannur'), ('KS', 'Kasaragod'), ('KL', 'Kollam'), ('KT', 'Kottayam'), ('KZ', 'Kozhikode'), ('MA', 'Malappuram'), ('PL', 'Palakkad'), ('PT', 'Pathanamthitta'), ('TV', 'Thiruvananthapuram'), ('TS', 'Thrissur'), ('WA', 'Wayanad')], max_length=2)),
                ('category', models.CharField(choices=[('cv', 'Covid'), ('nc', 'Non-Covid')], max_length=2)),
                ('status', models.CharField(choices=[('W', 'Waiting'), ('A', 'Admitted'), ('D', 'Discharged')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='BedAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('C', 'Covid'), ('N', 'Normal'), ('I', 'ICU'), ('V', 'Ventilator')], max_length=2)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beds.hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beds.patient')),
            ],
        ),
    ]
