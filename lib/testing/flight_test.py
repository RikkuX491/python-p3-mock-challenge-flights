import pytest

from classes.flight import Flight
from classes.customer import Customer
from classes.booking import Booking

class TestFlight:
    '''Flight in flight.py'''

    def test_has_airline(self):
        '''has the airline passed into __init__'''
        flight = Flight("Jetblue")

        assert flight.airline == "Jetblue"

    def test_validates_airline(self):
        '''has airline as unchangeable string'''
        with pytest.raises(Exception):
            Flight('')

        with pytest.raises(Exception):
            Flight(1)

        with pytest.raises(Exception):
            flight = Flight("American Airlines")
            flight.airline = "Delta Air Lines"

    def test_has_many_bookings(self):
        '''flight has many bookings'''
        flight = Flight("Jetblue")
        customer = Customer('Tom', 'Anderson')
        booking_1 = Booking(customer, flight, 2)
        booking_2 = Booking(customer, flight, 5)

        assert len(flight.bookings()) == 2
        assert booking_1 in flight.bookings()
        assert booking_2 in flight.bookings()

    def test_flight_bookings_type_booking(self):
        '''restaurant bookings are of type Booking'''
        flight = Flight("American Airlines")
        flight.bookings(1)
        assert not flight.bookings()
        customer = Customer('Henry', 'Smith')
        booking = Booking(customer, flight, 2)
        assert booking in flight.bookings()

    def test_has_many_flights(self):
        '''flight has many customers'''
        flight = Flight("American Airlines")
        customer = Customer('Alan', 'Turing')
        customer_2 = Customer('Albert', 'Einstein')
        Booking(customer, flight, 2)
        Booking(customer_2, flight, 5)

        assert len(flight.customers()) == 2
        assert customer in flight.customers()
        assert customer_2 in flight.customers()

    def test_flight_customers_type_customer(self):
        '''flight customers are of type Customer'''
        flight = Flight("Jetblue")
        flight.customers(1)
        assert not flight.customers()
        customer = Customer('Tom', 'Smith')
        flight.customers(customer)
        assert customer in flight.customers()

    def test_average(self):
        '''average_price() gets average of flight's booking prices'''
        flight = Flight("Jetblue")
        customer = Customer('Steve', 'Jobs')
        customer_2 = Customer('Bob', 'Hope')
        Booking(customer, flight, 2)
        Booking(customer_2, flight, 5)

        assert(flight.average_price() == 3.5)

    def test_get_all_flights(self):
        '''test has class attribute all'''
        Flight.all = []
        flight = Flight("Jetblue")
        flight_2 = Flight("Delta Air Lines")
        
        assert len(Flight.all) == 2
        assert flight in Flight.all
        assert flight_2 in Flight.all
