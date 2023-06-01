# Object Relations Mock Code Challenge - Flights

For this assignment, we'll be working with a Flight-style domain.

We have three models: `Flight`, `Customer`, and `Booking`.

For our purposes, a `Flight` has many `Bookings`, a `Customer` has many
`Booking`s, and a `Booking` belongs to a `Customer` and to a `Flight`.

`Flight` - `Customer` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You
can run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers, Readers, and Writers

For any invalid inputs raise an `Exception`. In your future work, you should
raise specific types of exceptions for specific error cases. You can do that
here and the tests will pass, but you don't have to this time around!

#### Customer

- `Customer __init__(self, first_name, last_name)`
  - Customer should be initialized with a first name and last name
- `Customer property first_name()` and `Customer property last_name()`
  - Return first and last name, respectively
  - Names must be of type `str`
  - Names must be between 1 and 25 characters, inclusive
  - `raise Exception` if setter validation fails

#### Flight

- `Flight __init__(self, airline)`
  - Flights should be initialized with an airline, as a string
- `Flight property airline()`
  - Returns the flight's airline
  - Must be 1 or more characters
  - Should not be able to change after the flight is created
  - `raise Exception` if setter validation fails
- `Flight class attribute all`
  - Returns a list of all flights

#### Booking

- `Booking __init__(self, customer, flight, price)`
  - Bookings should be initialized with a customer, flight, and a price (a number)
- `Booking property price()`
  - Returns the price for the booking
  - Price must be a number between 1 and 5, inclusive
  - `raise Exception` if setter validation fails

### Object Relationships

#### Booking

- `Booking customer`
  - Returns the customer object for that booking
  - Must be of type `Customer`
  - `raise Exception` if validation fails
  
- `Booking flight`
  - Returns the flight object for that given booking
  - Must be of type `Flight`
  - `raise Exception` if validation fails

#### Flight

- `Flight bookings(self, new_booking=None)`
  - Creates a new booking if called with new booking
  - Returns a list of all bookings for that flight
  - Bookings must be of type `Booking`
  - _Should be called from `Booking.__init__`_
- `Flight customers(self, new_customer=None)`
  - Creates a new customer if called with new customer
  - Returns a **unique** list of all customers who have booked a particular flight.
  - Customers must be of type `Customer`
  - _Should be called from `Booking.__init__`_

#### Customer

- `Customer flights(self, new_flight=None)`
  - Creates a new flight if called with new flight
  - Returns a **unique** list of all flights a customer has booked
  - Flights must be of type `Flight`
  - _Should be called from `Booking.__init__`_
- `Customer bookings(self, new_booking=None)`
  - Creates a new booking if called with new booking
  - Returns a list of all bookings a customer has made
  - _Should be called from `Booking.__init__`_

### Aggregate and Association Methods

#### Customer

- `Customer num_bookings()`
  - Returns the total number of bookings that a customer has made

#### Flight

- `Flight average_price(self)`
  - Returns the average price for a flight based on its bookings
  - Reminder: you can calculate the average by adding up all the prices and
    dividing by the number of prices
