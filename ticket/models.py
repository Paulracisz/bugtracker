from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class MyUser(AbstractUser):
    pass

class MyTicket(models.Model):
    title = models.CharField(max_length=50, default="")
    time_created = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=250, default="")
    TICKET_CHOICES = [
    ('NW', 'New'),
    ('CM', 'Completed'),
    ('IP', 'In Progress'),
    ('IV', 'Invalid'),
]
    status = models.CharField(max_length=300,
    choices=TICKET_CHOICES
        
    )
    ticket_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default="")
    ticket_assigned = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None, related_name='ticket_assigned', null=True, blank=True)
    completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None, related_name='completed_by', null=True, blank=True)
