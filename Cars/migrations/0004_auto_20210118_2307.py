# Generated by Django 3.1.5 on 2021-01-18 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0003_auto_20210112_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='description',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='litre',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='reservation',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='speed',
        ),
        migrations.AlterField(
            model_name='cars',
            name='stamp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Cars.marks', verbose_name='Марка и модель'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='transmission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Cars.transmissions', verbose_name='Коробка передач'),
        ),
    ]
