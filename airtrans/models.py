from django.db import models
from django.utils import timezone


class Booking(models.Model):

    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateField(auto_now_add=True)
    total_amount = models.FloatField(null=False)

    def __str__(self):
        return "{}".format(self.book_ref)


class Ticket(models.Model):

    ticket_no = models.PositiveIntegerField(primary_key=True)
    book_ref = models.ForeignKey(Booking, on_delete=models.CASCADE)
    passenger_id = models.PositiveIntegerField()
    passenger_name = models.CharField(max_length=100)
    contact_data = models.CharField(max_length=100)


class Airport(models.Model):

    airport_code = models.CharField(max_length=4, primary_key=True)
    airport_name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    coordinates = models.FloatField(null=False)
    # timezone =


class Flight(models.Model):

    flight_id = models.PositiveIntegerField(primary_key=True)
    # flight_no =
    # scheduled_departure =
    # scheduled_arrival =
    departure_airport = models.ForeignKey(Airport, related_name='departure_airport', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrival_airport', on_delete=models.CASCADE)
    # status =
    # aircraft_code =
    # actual_departure =
    # actual_arrival =


class Ticket_Flight(models.Model):

    ticket_no = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    fare_conditions = models.CharField(max_length=30)
    # amount = models.FloatField(null=False)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)


class Boarding_pass(models.Model):

    # ticket_no =
    # flight_id =
    boarding_no = models.PositiveIntegerField()
    seat_no = models.CharField(max_length=5)


class Aircraft(models.Model):

    # aircraft_code =
    model = models.CharField(max_length=30)
    range = models.CharField(max_length=30)


class Seat(models.Model):

    # aircraft_code =
    # seat_no =
    # fare_conditions =
    pass

# Create your models here.
