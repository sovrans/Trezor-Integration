# Generated by Django 2.1.5 on 2019-01-06 01:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crypto_auth', '0004_auto_20190105_1209'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction',
            new_name='Withdraw',
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='network',
            field=models.CharField(choices=[('https://etherscan.io/', 'MAINNET'), ('https://rinkeby.etherscan.io/', 'RINKEBY')], default='https://rinkeby.etherscan.io/', help_text='Network link', max_length=150),
        ),
    ]
