from . import views
from django.urls import path

app_name = 'bookingsystem'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('bookings/', views.BookingForm.as_view(), name='bookings'),
    path('menus/', views.Menus.as_view(), name='menus'),
    path('edit_bookings', views.editBooking.as_view(), name='edit_bookings'),
]
