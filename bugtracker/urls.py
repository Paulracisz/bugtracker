"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ticket import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('login/', views.login_view, name="loginview" ),
    path('logout/', views.logout_view, name='logoutview'),
    path('ticketdetail/<int:ticket_id>/', views.ticket_detail, name="ticketdetail"),
    path('userdetail/<int:user_id>/', views.user_detail),
    path('new_ticket/', views.add_ticket),
    path('edit_ticket/<int:ticket_id>/', views.ticket_edit),
    path('complete/<int:ticket_id>/', views.complete_ticket),
    path('invalid/<int:ticket_id>/', views.invalid_ticket),
    path('assign_ticket/<int:ticket_id>/', views.assign_ticket),
    path('admin/', admin.site.urls),
]
