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

To get started, run `pipenv install` while inside of this directory. Then run
`pipenv shell` to jump into the shell.

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

### Initializers and Properties

#### Customer

- `Customer __init__(self, first_name, last_name)`
  - Customer is initialized with a given name and family name
- `Customer property first_name` and `Customer property last_name`
  - Return first and last name, respectively
  - Names must be of type `str`
  - Names must be between 1 and 25 characters, inclusive
  - Names **can be** changed after the `Customer` object is initialized

#### Flight

- `Flight __init__(self, airline)`
  - Flight is initialized with an airline
- `Flight property airline`
  - Returns the flight's airline
  - Airlines must be of type `str`
  - Airlines must be 1 or more characters
  - Airlines **can be** changed after the `Flight` object is initialized

#### Booking

- `Booking __init__(self, customer, flight, price)`
  - Booking is initialized with a `Customer` instance, a `Flight` instance, and a price
- `Booking property price`
  - Returns the price for a flight
  - Prices must be of type `int`
  - Prices must be between 500 and 3000, inclusive
  - Prices **cannot be** changed after the `Booking` object is initialized

### Object Relationship Methods and Properties

#### Booking

- `Booking customer`
  - Returns the customer object for that booking
  - Must be of type `Customer`
  - Customers **can be** changed after the `Booking` object is initialized
- `Booking flight`
  - Returns the flight object for that booking
  - Must be of type `Flight`
  - Flights **can be** changed after the `Booking` object is initialized

#### Flight

- `Flight bookings()`
  - Returns a list of all bookings for that flight
  - Bookings must be of type `Booking`
- `Flight customers()`
  - Returns a **unique** list of all customers who have booked that flight.
  - Customers must be of type `Customer`

#### Customer

- `Customer bookings()`
  - Returns a list of all bookings a customer has made
  - Bookings must be of type `Booking`
- `Customer flights()`
  - Returns a **unique** list of all flights a customer has booked
  - Flights must be of type `Flight`

### Aggregate and Association Methods

#### Customer

- `Customer num_cheap_bookings()`
  - **Reminder**: a booking is considered cheap if its price is less than 1000
  - Returns the total number of cheap bookings that a customer has purchased
  - Returns `0` if the customer never purchased a cheap booking
- `Customer has_booked_flight(flight)`
  - Receives a `Flight` instance as argument
  - Returns `True` if the customer has made a booking for the given flight object
  - Returns `False` otherwise

#### Flight

- `Flight average_price()`
  - Returns the average price for a flight based on its bookings
  - Returns `0.0` if the customer has no bookings
  - Rounds the result to the first decimal digit
  - **Reminder**: you can calculate the average by adding up all the prices and
    dividing by the number of prices
- `Flight classmethod top_two_expensive_flights()`
  - Returns the top 2 expensive flights in descending order by average price
  - Flights must be of type `Flight`
  - Returns `None` if there are no bookings