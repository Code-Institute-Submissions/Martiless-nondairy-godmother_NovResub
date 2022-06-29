from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView
from .forms import OnlineForm
from django.contrib import messages
from django.urls import reverse_lazy



class Home(generic.DetailView):
    template_name = 'index.html'

    def get(self, request):
          return render(request, 'index.html')


class BookingForm(FormView):
    template_name = 'bookings.html'
    form_class = OnlineForm
    success_url = '/thank_you/'
    
    def booking_view(self, request):
        if request.method == 'POST':
            form = OnlineForm(request.POST)  
        return render(request, 'bookings.html')
        messages.success(request, "Thank you for booking with us. You will receive a confirmation email shortly.")


class ThankYou(generic.DetailView):
    template_name = 'thank_you.html'

    def get(self, request):
          return render(request, 'thank_you.html')

class Menus(generic.DetailView):
    template_name = 'menus.html'

    def get(self, request):
          return render(request, 'menus.html')


class Sign_in(generic.DetailView):

    def login_view(self, request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            return render(request, 'login.html')


#class BookingList(generic.ListView)

class editBooking(generic.DetailView):
    template_name = 'edit_bookings.html'

    def get(self, request):
        return render(request, 'edit_bookings.html')
