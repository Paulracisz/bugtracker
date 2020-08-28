from django import forms
from ticket.models import MyUser, MyTicket


class LogInForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class AddUserForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class AddTicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=250)

class EditTicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=250)

class AssignTicketForm(forms.Form):
     class Meta:
        model = MyTicket
        fields = ["ticket_assigned"]

    
