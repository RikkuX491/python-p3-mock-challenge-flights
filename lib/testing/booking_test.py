import pytest

from classes.flight import Flight
from classes.customer import Customer
from classes.booking import Booking

class TestBookings:
    '''Booking in booking.py'''

    def test_has_customer_flight_price(self):
        '''has the customer, flight, and price passed into __init__'''
        customer = Customer('Steve', 'Jobs')
        flight = Flight("Mels")
        booking = Booking(customer, flight, 2500)

        assert booking.customer == customer
        assert booking.flight == flight
        assert booking.price == 2500

    def test_validates_customer(self):
        '''checks to ensure customer is of type Customer'''
        flight = Flight("Delta Air Lines")
        
        with pytest.raises(Exception):
            Booking(1, flight, 2300)

    def test_validates_flight(self):
        '''checks to ensure flight is of type Flight'''
        customer = Customer('Rick', 'Jackson')
        
        with pytest.raises(Exception):
            Booking(customer, 1235, 2300)

    def test_validates_price(self):
        '''checks to ensure price is integer between 1 and 5, inclusive'''
        customer = Customer('Steve', 'Wayne')
        flight = Flight("Jetblue")

        with pytest.raises(Exception):
            Booking(customer, flight, 450)

        with pytest.raises(Exception):
            Booking(customer, flight, 4000)
