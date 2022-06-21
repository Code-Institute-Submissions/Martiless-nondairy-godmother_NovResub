from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Booking


class Home(generic.DetailView):
    template_name = 'index.html'

    def get(self, request):
          return render(request, 'index.html')


#class BookingForm(generic.FormView):
#    form = Booking
#    template_name = 'bookings.html'


#class Menus(generic.DetailView):
#    template_name = 'menus.html'


#class Login(generic.DetailView):
#    template_name = 'login.html'
