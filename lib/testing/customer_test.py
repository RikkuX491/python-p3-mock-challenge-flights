import pytest

from classes.many_to_many import Flight
from classes.many_to_many import Customer
from classes.many_to_many import Booking


class TestCustomer:
    """Customer in many_to_many.py"""

    def test_has_names(self):
        """Customer is initialized with first name and last name"""
        customer = Customer("Alice", "Smith")
        assert customer.first_name == "Alice"
        assert customer.last_name == "Smith"

    def test_names_are_mutable_strings(self):
        """names must be of type str and mutable"""
        customer_1 = Customer("Bruce", "Wayne")

        assert isinstance(customer_1.first_name, str)
        assert isinstance(customer_1.last_name, str)

        customer_1.first_name = "Cindy"
        customer_1.last_name = 7
        customer_1.first_name = 7
        assert customer_1.first_name == "Cindy"
        assert customer_1.last_name == "Wayne"

    def test_names_are_valid(self):
        """first and last names must be between 1 and 25 characters, inclusive"""
        customer = Customer("Daniel", "Jones")

        assert 1 <= len(customer.first_name) <= 25
        assert 1 <= len(customer.last_name) <= 25

        customer.first_name = "D" * 77
        customer.first_name = ""
        customer.last_name = "D" * 77
        customer.last_name = ""
        assert customer.first_name == "Daniel"
        assert customer.last_name == "Jones"

    def test_has_many_bookings(self):
        """customer has many bookings"""
        flight = Flight("jetBlue")
        customer = Customer("Edward", "Jackson")
        booking_1 = Booking(customer, flight, 900)
        booking_2 = Booking(customer, flight, 2000)

        assert len(customer.bookings()) == 2
        assert booking_1 in customer.bookings()
        assert booking_2 in customer.bookings()

    def test_bookings_of_type_booking(self):
        """bookings must be of type Booking"""
        customer = Customer("Frank", "Anderson")
        flight = Flight("Delta Air Lines")
        Booking(customer, flight, 2000)
        Booking(customer, flight, 900)

        assert isinstance(customer.bookings()[0], Booking)
        assert isinstance(customer.bookings()[1], Booking)

    def test_has_many_flights(self):
        """customer has many flights."""
        flight = Flight("jetBlue")
        flight_2 = Flight("Delta Air Lines")
        flight_3 = Flight("Hawaiian Airlines")
        customer = Customer("George", "Jackson")
        Booking(customer, flight, 900)
        Booking(customer, flight_2, 2000)

        assert flight in customer.flights()
        assert flight_2 in customer.flights()
        assert flight_3 not in customer.flights()

    def test_flights_of_type_flight(self):
        """flights must of type Flight"""
        flight_1 = Flight("jetBlue")
        flight_2 = Flight("Delta Air Lines")

        customer = Customer("Hugh", "Kim")
        Booking(customer, flight_1, 900)
        Booking(customer, flight_2, 2000)

        assert isinstance(customer.flights()[0], Flight)
        assert isinstance(customer.flights()[1], Flight)

    def test_flights_unique(self):
        """customer flights are unique"""
        flight_1 = Flight("jetBlue")
        flight_2 = Flight("Delta Air Lines")

        customer = Customer("Ian", "Thompson")
        Booking(customer, flight_1, 900)
        Booking(customer, flight_2, 2000)
        Booking(customer, flight_2, 1500)

        assert len(set(customer.flights())) == len(customer.flights())
        assert len(customer.flights()) == 2
        assert flight_1 in customer.flights()
        assert flight_2 in customer.flights()

    def test_num_cheap_bookings(self):
        """returns the total number of cheap bookings by that customer"""
        flight_1 = Flight("jetBlue")
        flight_2 = Flight("Delta Air Lines")
        customer_1 = Customer("Jack", "Jones")
        customer_2 = Customer("Kimberly", "Anderson")
        customer_3 = Customer("Lawrence", "Jackson")
        Booking(customer_1, flight_1, 900)
        Booking(customer_1, flight_2, 1500)
        Booking(customer_1, flight_1, 600)
        Booking(customer_2, flight_2, 1500)
        Booking(customer_2, flight_1, 900)
        Booking(customer_3, flight_1, 1500)

        assert customer_1.num_cheap_bookings() == 2
        assert customer_2.num_cheap_bookings() == 1
        assert customer_3.num_cheap_bookings() == 0

    def test_has_booked_flight(self):
        """returns True if the customer booked the flight, else False"""
        flight_1 = Flight("jetBlue")
        flight_2 = Flight("Delta Air Lines")
        customer_1 = Customer("Mary", "Jackson")
        Booking(customer_1, flight_1, 900)

        assert customer_1.has_booked_flight(flight_1) == True
        assert customer_1.has_booked_flight(flight_2) == False