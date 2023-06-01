from classes.flight import Flight
from classes.customer import Customer
from classes.booking import Booking
import pytest

class TestBookings:
    '''Booking in booking.py'''

    def test_has_price(self):
        '''has the price passed into __init__'''
        flight = Flight("Alaska Airlines")
        customer = Customer('Tom', 'Jackson')
        booking_1 = Booking(customer, flight, 524)
        booking_2 = Booking(customer, flight, 2354)

        assert(booking_1.price == 524)
        assert(booking_2.price == 2354)
        with pytest.raises(Exception):
            booking_1.price = 6000
        with pytest.raises(Exception):
            booking_1.price = "2000"
        with pytest.raises(Exception):
            booking_1.price = -300

    def test_has_a_customer(self):
        '''booking has a customer'''
        flight = Flight("Jetblue")
        customer = Customer('Steve', 'Jobs')
        booking_1 = Booking(customer, flight, 2500)
        booking_2 = Booking(customer, flight, 655)

        assert(booking_1.customer == customer)
        assert(booking_2.customer == customer)

    def test_has_a_flight(self):
        '''Booking has a flight.'''
        flight = Flight("American Airlines")
        customer = Customer('Steve', 'Jobs')
        customer_2 = Customer('Jack', 'Smith')
        booking_1 = Booking(customer, flight, 2500)
        booking_2 = Booking(customer_2, flight, 1500)

        assert(booking_1.flight == flight)
        assert(booking_2.flight == flight)
