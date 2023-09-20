import pytest

from classes.many_to_many import Flight
from classes.many_to_many import Customer
from classes.many_to_many import Booking


class TestFlight:
    """Flight in many_to_many.py"""

    def test_has_airline(self):
        """Flight is initialized with an airline"""
        flight = Flight("jetBlue")

        assert flight.airline == "jetBlue"

    def test_airline_is_mutable_string(self):
        """airline is a mutable string"""
        flight = Flight("jetBlue")
        flight.airline = "Delta Air Lines"

        assert flight.airline == "Delta Air Lines"
        assert isinstance(flight.airline, str)

        flight.airline = 7
        assert flight.airline == "Delta Air Lines"

    def test_airline_is_valid(self):
        """airline must be 1 or more characters long"""
        flight = Flight("jetBlue")
        assert len(flight.airline) > 0
        
        flight.airline = ""
        assert flight.airline == "jetBlue"

    def test_has_many_bookings(self):
        """flight has many bookings"""
        flight = Flight("jetBlue")
        customer = Customer("Alice", "Smith")
        booking_1 = Booking(customer, flight, 900)
        booking_2 = Booking(customer, flight, 2000)

        assert len(flight.bookings()) == 2
        assert booking_1 in flight.bookings()
        assert booking_2 in flight.bookings()

    def test_bookings_of_type_booking(self):
        """flight bookings are of type Booking"""
        flight = Flight("jetBlue")
        customer = Customer("Barry", "Jackson")
        Booking(customer, flight, 900)
        Booking(customer, flight, 2000)

        assert isinstance(flight.bookings()[0], Booking)
        assert isinstance(flight.bookings()[1], Booking)

    def test_has_many_customers(self):
        """flight has many customers"""
        flight = Flight("jetBlue")
        customer = Customer("Cindy", "Jackson")
        customer_2 = Customer("Dylan", "Jones")
        Booking(customer, flight, 900)
        Booking(customer_2, flight, 2000)

        assert len(flight.customers()) == 2
        assert customer in flight.customers()
        assert customer_2 in flight.customers()

    def test_customers_of_type_customer(self):
        """customers must be of type Customer"""
        flight = Flight("jetBlue")
        customer = Customer("Ernie", "Jackson")
        customer_2 = Customer("Frank", "Anderson")
        Booking(customer, flight, 900)
        Booking(customer_2, flight, 2000)

        assert isinstance(flight.customers()[0], Customer)
        assert isinstance(flight.customers()[1], Customer)

    def test_customers_are_unique(self):
        """customers are unique"""
        flight = Flight("jetBlue")
        customer_1 = Customer("Gregory", "Anderson")
        customer_2 = Customer("Hugh", "Jones")
        Booking(customer_1, flight, 900)
        Booking(customer_2, flight, 2000)
        Booking(customer_1, flight, 1500)

        assert len(set(flight.customers())) == len(flight.customers())
        assert len(flight.customers()) == 2
        assert customer_1 in flight.customers()
        assert customer_2 in flight.customers()

    def test_average_price(self):
        """returns average of flight's booking prices"""
        flight = Flight("jetBlue")
        customer = Customer("Ian", "Jackson")
        customer_2 = Customer("Jack", "Smith")
        Booking(customer, flight, 900)
        Booking(customer_2, flight, 2000)
        Booking(customer_2, flight, 1750)

        # rounds the result to 1 decimal place
        assert flight.average_price() == 1550.0
        
        Booking.all = []
        assert flight.average_price() == 0.0

    def test_top_two_expensive_flights(self):
        """returns the top 2 expensive flights in descending order by average price"""
        Booking.all = []
        flight_1 = Flight("jetBlue")
        flight_2 = Flight("Delta Air Lines")
        flight_3 = Flight("Hawaiian Airlines")
        flight_4 = Flight("Alaskan Airlines")
        customer = Customer("Alice", "Smith")
        customer_2 = Customer("Bruce", "Jackson")
        Booking(customer, flight_1, 2000)
        Booking(customer, flight_2, 1750)
        Booking(customer, flight_3, 1500)
        Booking(customer, flight_4, 900)
        Booking(customer_2, flight_1, 2000)
        Booking(customer_2, flight_2, 2000)
        Booking(customer_2, flight_3, 2000)

        assert flight_1 in Flight.top_two_expensive_flights()
        assert flight_2 in Flight.top_two_expensive_flights()
        assert flight_3 not in Flight.top_two_expensive_flights()
        assert flight_4 not in Flight.top_two_expensive_flights()

        Booking.all = []
        assert Flight.top_two_expensive_flights() is None