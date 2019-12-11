# Generated by Django 3.0 on 2019-12-11 03:51

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='modificado em'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='modificado em'),
        ),
    ]
