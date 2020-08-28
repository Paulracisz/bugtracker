# Generated by Django 3.1 on 2020-08-26 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20200826_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myticket',
            name='ticket_assigned',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_assigned', to=settings.AUTH_USER_MODEL),
        ),
    ]
