from classes.customer import Customer
from classes.flight import Flight

class Booking:
    
    def __init__(self, customer, flight, price):
        self.customer = customer
        self.flight = flight
        self.price = price