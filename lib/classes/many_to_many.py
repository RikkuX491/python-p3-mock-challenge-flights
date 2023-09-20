class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def bookings(self):
        pass
    
    def flights(self):
        pass

    def num_cheap_bookings(self):
        pass

    def has_booked_flight(self, flight):
        pass

class Flight:
    def __init__(self, airline):
        self.airline = airline
        
    def bookings(self):
        pass
    
    def customers(self):
        pass

    def average_price(self):
        pass

    @classmethod
    def top_two_expensive_flights(cls):
        pass

class Booking:    
    def __init__(self, customer, flight, price):
        self.customer = customer
        self.flight = flight
        self.price = price
