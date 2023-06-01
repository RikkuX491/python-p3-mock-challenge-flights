import pytest

from classes.flight import Flight
from classes.customer import Customer
from classes.booking import Booking

class TestCustomer:
    '''Customer in customer.py'''

    def test_has_name(self):
        '''has the first name and last name passed into __init__'''
        customer = Customer('Alex', 'Smith')
        assert customer.first_name == "Alex"
        assert customer.last_name == "Smith"

    def test_validates_name(self):
        '''has first and last names as strings between 1 and 25 characters, inclusive'''
        with pytest.raises(Exception):
            Customer('', 'Johnson')

        with pytest.raises(Exception):
            Customer('Bruce', '')

        with pytest.raises(Exception):
            Customer('B' * 26, 'Johnson')

        with pytest.raises(Exception):
            Customer('Bruce', 'J' * 26)

        with pytest.raises(Exception):
            Customer(1, 'Johnson')

        with pytest.raises(Exception):
            Customer('Bruce', 2)

    def test_has_many_bookings(self):
        '''customer has many bookings'''
        flight = Flight("American Airlines")
        customer = Customer('Chris', 'Jackson')
        booking_1 = Booking(customer, flight, 2000)
        booking_2 = Booking(customer, flight, 2500)

        assert len(customer.bookings()) == 2
        assert booking_1 in customer.bookings()
        assert booking_2 in customer.bookings()

    def test_bookings_must_be_booking_type(self):
        '''customer bookings are of type Booking'''
        customer = Customer("David", "Stevenson")
        customer.bookings(1)
        assert not customer.bookings()
        flight = Flight("Jetblue")
        booking = Booking(customer, flight, 1550)
        customer.bookings(booking)
        assert booking in customer.bookings()

    def test_has_many_flights(self):
        '''customer has many flights.'''
        flight = Flight("Hawaiian Airlines")
        flight_2 = Flight("Delta Air Lines")

        customer = Customer('Ernie', 'Thompson')
        Booking(customer, flight, 2500)
        Booking(customer, flight_2, 1500)

        assert flight in customer.flights()
        assert flight_2 in customer.flights()

    def test_flights_must_be_flight_type(self):
        '''customer flights are of type Flight'''
        customer = Customer("Frank", "Davidson")
        customer.flights(1)
        assert not customer.flights()
        flight = Flight("Alaskan Airlines")
        customer.flights(flight)
        assert flight in customer.flights()

    def test_customer_flights_unique(self):
        '''customer flights are unique'''
        customer = Customer("Greg", "Stevenson")
        flight = Flight("American Airlines")
        customer.flights(flight)
        assert flight in customer.flights() and len(customer.flights()) == 1
        customer.flights(flight)
        assert len(customer.flights()) == 1


    def test_get_number_of_bookings(self):
        '''test get_number_of_bookings()'''
        flight = Flight("Spirit Airlines")
        customer = Customer('Steve', 'Jobs')
        Booking(customer, flight, 2500)
        Booking(customer, flight, 1000)

        assert customer.num_bookings() == 2
