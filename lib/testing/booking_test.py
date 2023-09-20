import pytest

from classes.many_to_many import Flight
from classes.many_to_many import Customer
from classes.many_to_many import Booking


class TestBooking:
    """Booking in many_to_many.py"""

    def test_has_price(self):
        """Booking is initialized with a price"""
        flight = Flight("jetBlue")
        customer = Customer("Alice", "Smith")
        booking_1 = Booking(customer, flight, 900)
        booking_2 = Booking(customer, flight, 2000)

        assert booking_1.price == 900
        assert booking_2.price == 2000

    def test_price_is_immutable(self):
        """price is immutable"""
        flight = Flight("jetBlue")
        customer = Customer("Alice", "Smith")
        booking_1 = Booking(customer, flight, 900)

        booking_1.price = 600
        assert booking_1.price == 900