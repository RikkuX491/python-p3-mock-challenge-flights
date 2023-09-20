class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.bookings_list = []
        self.flights_list = []
        
    def bookings(self):
        return self.bookings_list
    
    def flights(self):
        return self.flights_list

    def num_cheap_bookings(self):
        cheap_bookings = [booking for booking in self.bookings_list if booking.price < 1000]
        return len(cheap_bookings)

    def has_booked_flight(self, flight):
        if flight in self.flights_list:
            return True
        else:
            return False

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name_parameter):
        if type(first_name_parameter) == str and 1 <= len(first_name_parameter) <= 25:
            self._first_name = first_name_parameter

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name_parameter):
        if type(last_name_parameter) == str and 1 <= len(last_name_parameter) <= 25:
            self._last_name = last_name_parameter

class Flight:
    
    all = []

    def __init__(self, airline):
        self.airline = airline
        self.bookings_list = []
        self.customers_list = []

        Flight.all.append(self)
        
    def bookings(self):
        return self.bookings_list
    
    def customers(self):
        return self.customers_list

    def average_price(self):
        if len([booking for booking in Booking.all if booking.flight is self]) == 0:
            return 0.0
        else:
            prices_list = [booking.price for booking in self.bookings_list]
            return round(sum(prices_list) / len(prices_list), 1)

    @classmethod
    def top_two_expensive_flights(cls):
        if len(Booking.all) == 0:
            return None
        else:
            cls.all.sort(reverse=True, key=lambda f: f.average_price())
            return cls.all[0:2]

    @property
    def airline(self):
        return self._airline
    
    @airline.setter
    def airline(self, airline_parameter):
        if type(airline_parameter) == str and len(airline_parameter) >= 1:
            self._airline = airline_parameter

class Booking:

    all = []

    def __init__(self, customer, flight, price):
        self.customer = customer
        self.flight = flight
        self.price = price

        self.flight.bookings_list.append(self)

        if not (customer in self.flight.customers_list):
            self.flight.customers_list.append(customer)

        self.customer.bookings_list.append(self)

        if not (flight in self.customer.flights_list):
            self.customer.flights_list.append(flight)
        
        Booking.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price_parameter):
        if (not hasattr(self, 'price')) and type(price_parameter) == int and 500 <= price_parameter <= 3000:
            self._price = price_parameter

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer_parameter):
        if type(customer_parameter) == Customer:
            self._customer = customer_parameter

    @property
    def flight(self):
        return self._flight
    
    @flight.setter
    def flight(self, flight_parameter):
        if type(flight_parameter) == Flight:
            self._flight = flight_parameter