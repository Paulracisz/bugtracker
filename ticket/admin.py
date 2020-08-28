from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ticket.models import MyUser, MyTicket

# Register your models here.
admin.site.register(MyUser, UserAdmin),
admin.site.register(MyTicket)