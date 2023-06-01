class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._flights = []
        self._bookings = []
        
    def bookings(self, new_booking=None):
        from classes.booking import Booking
        if isinstance(new_booking, Booking):
            self._bookings.append(new_booking)
        return self._bookings
    
    def flights(self, new_flight=None):
        from classes.flight import Flight
        if isinstance(new_flight, Flight):
            self._flights.append(new_flight)
        return list(set(self._flights))

    def num_bookings(self):
        return len(self._bookings)

    def get_first_name(self):
        return self._first_name
    
    def set_first_name(self, first_name):
        if isinstance(first_name, str) and 1 <= len(first_name) <= 25:
            self._first_name = first_name
        else:
            raise Exception("Invalid value for first name!")
        
    def get_last_name(self):
        return self._last_name
    
    def set_last_name(self, last_name):
        if type(last_name) == str and 1 <= len(last_name) <= 25:
            self._last_name = last_name
        else:
            raise Exception("Invalid value for last name!")

    first_name = property(get_first_name, set_first_name)
    last_name = property(get_last_name, set_last_name)