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

    def test_price_is_valid_int(self):
        """price must be of type int and between 500 and 3000"""
        flight = Flight("jetBlue")
        customer = Customer("Bruce", "Smith")
        booking_1 = Booking(customer, flight, 1750)

        assert isinstance(booking_1.price, int)
        assert 500 <= booking_1.price <= 3000

    def test_has_a_customer(self):
        """booking has a customer"""
        flight = Flight("jetBlue")
        customer = Customer("Candice", "Jordan")
        booking_1 = Booking(customer, flight, 900)
        booking_2 = Booking(customer, flight, 2000)

        assert booking_1.customer == customer
        assert booking_2.customer == customer

    def test_customer_of_type_customer_and_mutable(self):
        """customer must be of type Customer and mutable"""

        flight = Flight("jetBlue")
        customer_1 = Customer("Barry", "Jackson")
        customer_2 = Customer("Barry", "Jameson")
        booking_1 = Booking(customer_1, flight, 900)
        booking_2 = Booking(customer_1, flight, 2000)

        booking_1.customer = "Batman"

        assert isinstance(booking_1.customer, Customer)
        assert isinstance(booking_2.customer, Customer)
        assert booking_1.customer == customer_1
        
        booking_1.customer = customer_2
        assert booking_1.customer.last_name == "Jameson"
        assert isinstance(booking_2.customer, Customer)

    def test_has_a_flight(self):
        """booking has a flight"""
        flight = Flight("jetBlue")
        customer = Customer("Tom", "Jones")
        customer_2 = Customer("Shirley", "Smith")
        booking_1 = Booking(customer, flight, 900)
        booking_2 = Booking(customer_2, flight, 2000)

        assert booking_1.flight == flight
        assert booking_2.flight == flight

    def flight_of_type_flight_and_mutable(self):
        """flight must be of type Flight and mutable"""
        flight_1 = Flight("jetBlue")
        flight_2 = Flight("Delta Air Lines")
        customer = Customer("Kelly", "Thompson")
        booking_1 = Booking(customer, flight_1, 900)
        booking_2 = Booking(customer, flight_2, 2000)

        assert isinstance(booking_1.flight, Flight)
        assert isinstance(booking_2.flight, Flight)

        booking_1.flight = flight_2
        assert booking_1.flight.airline == "jetBlue"
        assert isinstance(booking_2.flight, Flight)

    def test_has_all_property(self):
        """Booking class has an all property"""
        Booking.all = []
        flight = Flight("jetBlue")
        customer = Customer("Susan", "Jordan")
        booking_1 = Booking(customer, flight, 900)
        booking_2 = Booking(customer, flight, 2000)

        assert len(Booking.all) == 2
        assert booking_1 in Booking.all
        assert booking_2 in Booking.all