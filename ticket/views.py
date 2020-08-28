from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponseForbidden
from ticket.forms import LogInForm, AddTicketForm, EditTicketForm, AssignTicketForm
from django.contrib.auth import login, logout, authenticate
from ticket.models import MyUser, MyTicket


# Got help from Matt and Ruben

# Create your views here.
@login_required
def index(request):
    tickets = MyTicket.objects.all()
    tickets_completed = tickets.filter(status='CM')
    tickets_invalid = tickets.filter(status='IV')
    tickets_in_progress = tickets.filter(status='IP')
    tickets_new = tickets.filter(status='NW')
    return render(request,"index.html", 
                  {"tickets": tickets, 
                    "tickets_completed": tickets_completed,
                    "tickets_invalid": tickets_invalid,
                    "tickets_in_progress": tickets_in_progress,
                    "tickets_new": tickets_new,
                  })


def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = LogInForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def ticket_detail(request, ticket_id):
    ticket = MyTicket.objects.filter(id=ticket_id).first()
    return render(request, "ticketdetail.html", {"ticket": ticket})

def add_ticket(request):
    if request.method == "POST":
            form = AddTicketForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_ticket = MyTicket.objects.create(description=data.get("description"), title=data.get("title"), ticket_by=request.user, status='NW')
            return HttpResponseRedirect(reverse("homepage"))
    form = AddTicketForm()
    return render(request, "new_ticket.html", {"form": form}) 

def ticket_edit(request, ticket_id):
    ticket = MyTicket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = EditTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data["title"]
            ticket.description = data["description"]
            ticket.save()
        return HttpResponseRedirect(reverse("ticketdetail", args=[ticket.id]))
    data = {
        "title": ticket.title,
        "description": ticket.description,
    }
    form = EditTicketForm(initial=data)
    return render(request, "edit_ticket.html", {"form": form})

def user_detail(request, user_id):
    user = MyUser.objects.get(id=user_id)
    owned_tickets = MyTicket.objects.filter(ticket_by=user)
    tickets_assigned = MyTicket.objects.filter(ticket_assigned=user)
    completed = MyTicket.objects.filter(completed_by=user)

    return render(request, "userdetail.html", {"tickets": owned_tickets, "user": user, "tickets_assigned": tickets_assigned, "completed": completed})


def assign_ticket(request, ticket_id):
    ticket = MyTicket.objects.get(id=ticket_id)
    ticket.status = 'IP'
    ticket.completed_by = None
    if request.method == "POST":
        form = AssignTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.ticket_assigned = data["ticket_assigned"]
            ticket.save()
        return HttpResponseRedirect(reverse("ticketdetail", args=[ticket.id]))
    data = {
        "ticket_assigned": ticket.ticket_assigned,
    }
    form = AssignTicketForm(initial=data)
    return render(request, "generic_form.html", {"form": form})

def complete_ticket(request, ticket_id):
    ticket = MyTicket.objects.get(id=ticket_id)
    ticket.status = 'CM'
    ticket.completed_by = ticket.ticket_assigned
    ticket.ticket_assigned = None
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def invalid_ticket(request, ticket_id):
    ticket = MyTicket.objects.get(id=ticket_id)
    ticket.status = 'IV'
    ticket.ticket_assigned = None
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

