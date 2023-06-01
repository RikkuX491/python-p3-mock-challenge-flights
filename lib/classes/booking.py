from classes.customer import Customer
from classes.flight import Flight

class Booking:
    
    def __init__(self, customer, flight, price):
        self.customer = customer
        self.flight = flight
        self.price = price

        self.flight.bookings(self)
        self.flight.customers(self.customer)
        self.customer.flights(self.flight)
        self.customer.bookings(self)

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if isinstance(price, int) and 500 <= price <= 3000:
            self._price = price
        else:
            raise Exception("Invalid value for price!")
        
    def get_customer(self):
        return self._customer
    
    def set_customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Invalid value for customer!")
        
    def get_flight(self):
        return self._flight
    
    def set_flight(self, flight):
        if isinstance(flight, Flight):
            self._flight = flight
        else:
            raise Exception("Invalid value for flight!")

    price = property(get_price, set_price)
    customer = property(get_customer, set_customer)
    flight = property(get_flight, set_flight)