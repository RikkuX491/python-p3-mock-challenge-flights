class Flight:

    all = []

    def __init__(self, airline):
        self.airline = airline

        self._bookings = []
        self._customers = []

        Flight.all.append(self)
        
    def bookings(self, new_booking=None):
        from classes.booking import Booking
        if isinstance(new_booking, Booking):
            self._bookings.append(new_booking)
        return self._bookings
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if isinstance(new_customer, Customer):
            self._customers.append(new_customer)
        return list(set(self._customers))

    def average_price(self):
        prices = [booking.price for booking in self._bookings]
        return sum(prices) / len(prices)

    def get_airline(self):
        return self._airline
    
    def set_airline(self, airline):
        if (not hasattr(self, "airline")) and isinstance(airline, str) and len(airline) >= 1:
            self._airline = airline
        else:
            raise Exception("Cannot change airline or invalid value for airline!")

    airline = property(get_airline, set_airline)