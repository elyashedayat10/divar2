# Generated by Django 3.2.14 on 2022-07-11 06:33

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('wantads', '0007_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='created',
            field=django_jalali.db.models.jDateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='updated',
            field=django_jalali.db.models.jDateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='created',
            field=django_jalali.db.models.jDateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated',
            field=django_jalali.db.models.jDateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='created',
            field=django_jalali.db.models.jDateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='updated',
            field=django_jalali.db.models.jDateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='viewed',
            name='created',
            field=django_jalali.db.models.jDateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='viewed',
            name='updated',
            field=django_jalali.db.models.jDateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='wantad',
            name='created',
            field=django_jalali.db.models.jDateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wantad',
            name='updated',
            field=django_jalali.db.models.jDateField(auto_now=True),
        ),
    ]
