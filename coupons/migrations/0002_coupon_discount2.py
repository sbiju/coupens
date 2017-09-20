# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='discount2',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
    ]
