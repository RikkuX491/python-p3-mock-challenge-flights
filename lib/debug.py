#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker
import ipdb

from classes.customer import Customer
from classes.flight import Flight
from classes.booking import Booking

if __name__ == '__main__':
    fake = Faker()

    FLIGHT_NAMES = ["American Airlines", "Delta Air Lines", "British Airways", "Southwest Airlines", "Alaska Airlines", "Emirates", "United Airlines", "Jetblue", "Air Canada", "Hawaiian Airlines"]

    customers = [Customer(fake.first_name(), fake.last_name()) for i in range(50)]
    flights = [Flight(rc(FLIGHT_NAMES)) for i in range(25)]
    bookings = [Booking(rc(customers), rc(flights), randint(500, 3000)) for i in range(200)]

    ipdb.set_trace()
