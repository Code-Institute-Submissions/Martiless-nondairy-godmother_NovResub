# Generated by Django 3.2.13 on 2022-07-31 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0006_alter_booking_number_of_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_of_people',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', help_text='\n For parties of more than 10, please call us on 021 4569 782', max_length=2),
        ),
    ]
