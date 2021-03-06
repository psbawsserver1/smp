# Generated by Django 3.1.1 on 2020-10-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project', models.CharField(blank=True, max_length=50, null=True)),
                ('System_RID_No', models.CharField(blank=True, max_length=30, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('RunTime_Hrs', models.FloatField(blank=True, null=True)),
                ('Water_Discharge_Lts', models.FloatField(blank=True, null=True)),
                ('Pump_Consumption_KWH', models.FloatField(blank=True, null=True)),
                ('Inverter_Input_KWH', models.FloatField(blank=True, null=True)),
                ('Inverter_Output_KWH', models.FloatField(blank=True, null=True)),
                ('Total_KWH_Generation', models.FloatField(blank=True, null=True)),
                ('Gross_KWH', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='md',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project', models.CharField(blank=True, max_length=50, null=True)),
                ('System_RID_No', models.CharField(blank=True, max_length=30, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('RunTime_Hrs', models.FloatField(blank=True, null=True)),
                ('Water_Discharge_Lts', models.FloatField(blank=True, null=True)),
                ('Pump_Consumption_KWH', models.FloatField(blank=True, null=True)),
                ('Inverter_Input_KWH', models.FloatField(blank=True, null=True)),
                ('Inverter_Output_KWH', models.FloatField(blank=True, null=True)),
                ('Total_KWH_Generation', models.FloatField(blank=True, null=True)),
                ('Gross_KWH', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='siteDtls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sid', models.CharField(blank=True, max_length=30, null=True)),
                ('ConNum', models.IntegerField(blank=True, null=True)),
                ('ConName', models.CharField(blank=True, max_length=30, null=True)),
                ('ConMob', models.IntegerField(blank=True, max_length=10, null=True)),
                ('LocName', models.CharField(blank=True, max_length=30, null=True)),
                ('PumpDtls', models.CharField(blank=True, max_length=30, null=True)),
                ('InvDtls', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
