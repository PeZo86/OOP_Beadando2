"""
class Flight:

    def __init__(self):

        self.flight = {

            101: {'arrival': 'Rome', 'price': 15000, 'booked': False, 'guest': None},
            102: {'arrival': 'Catania', 'price': 25000, 'booked': False, 'guest': None},
            201: {'arrival': 'Paris', 'price': 23500, 'booked': False, 'guest': None},
            310: {'arrival': 'London', 'price': 35000, 'booked': False, 'guest': None},
            501: {'arrival': 'Debrecen', 'price': 5000, 'booked': False, 'guest': None},
            502: {'arrival': 'Szeged', 'price': 7500, 'booked': False, 'guest': None},
        }

"""

from abc import ABC, abstractmethod

class Flight(ABC):

    def __init__(self, flight_no, arrival, price):

        self.flight_no = flight_no,

        self.arrival = arrival,

        self.price = price,

    def flight_type(self):

        pass

    def __repr__(self):

        return f"{self.flight_type()} Járat #{self.flight_no} -> {self.arrival}, Ár: {self.price}"

class NationalFlight(Flight):

    def flight_type(self):

        return "Belföldi"

class InternationalFlight(Flight):

    def flight_type(self):

        return "Nemzetközi"




    def run(self):

        while True:

            print("\nWelcome to Simple Booking App")

            print("1. View available flights")

            print("2. Book flight")

            print("3. Check flight")

            print("4. Cancel flight")

            print("5. Exit")

            try:

                choice = int(input("Enter your choice: "))

                if choice == 1:

                    self.view_available_flights()

                elif choice == 2:

                    self.book_flight()

                elif choice == 3:

                    self.check_flight()

                elif choice == 4:

                    self.cancel_flight()

                elif choice == 5:

                    print("\nThank you for using Simple Booking App. Goodbye!")

                    break

                else:

                    print("\nInvalid choice. Please enter a valid choice.")

            except ValueError:

                print("\nInvalid input. Please enter a number between 1 and 5.")

if __name__ == '__main__':

    flight = Flight()

    flight.run()


