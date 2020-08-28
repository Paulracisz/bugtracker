# Generated by Django 3.1 on 2020-08-26 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20200826_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myticket',
            name='completed_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='completed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='myticket',
            name='ticket_assigned',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_assigned', to=settings.AUTH_USER_MODEL),
        ),
    ]
