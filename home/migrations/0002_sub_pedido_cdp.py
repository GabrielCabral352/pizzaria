# Generated by Django 3.2.7 on 2021-10-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_pedido',
            name='cdp',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
