# Generated by Django 3.2.7 on 2021-10-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('bebida', 'bebida'), ('comida', 'comida'), ('naodeclarado', 'naodeclarado')], default='naodeclarado', max_length=255)),
            ],
        ),
    ]
