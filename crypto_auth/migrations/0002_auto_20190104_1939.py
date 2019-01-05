# Generated by Django 2.1.4 on 2019-01-04 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hloruser',
            options={'verbose_name': 'Users of Hlor', 'verbose_name_plural': 'Users of Hlor'},
        ),
        migrations.AlterField(
            model_name='hloruser',
            name='balance',
            field=models.DecimalField(decimal_places=18, default='0', help_text='User Balance', max_digits=1000),
        ),
    ]
