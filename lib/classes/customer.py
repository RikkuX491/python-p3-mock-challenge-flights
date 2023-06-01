class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def bookings(self, new_booking=None):
        from classes.booking import Booking
        pass
    
    def flights(self, new_flight=None):
        from classes.flight import Flight
        pass

    def num_bookings(self):
        pass
