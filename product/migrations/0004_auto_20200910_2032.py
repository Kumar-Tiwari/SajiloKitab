# Generated by Django 3.1.1 on 2020-09-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200909_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug_field',
            field=models.SlugField(default='', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('School Level', 'School Level'), ('Bachelor Level', 'Bachelor Level'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]
