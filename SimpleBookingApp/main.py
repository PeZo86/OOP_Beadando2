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

    def view_available_flights(self):

        print("\nAvailable flights:")

        for flight_no, details in self.flight.keys():

            if not details['booked']:

                print(f"Flight {flight_no}: {details['arrival']} - {details['price']}")

    def book_flight(self, flight_no):

        self.view_available_flights()

        try:

            flight_no = int(input("Enter flight no: "))

            if flight_no in self.flight.keys() and not self.flight[flight_no]['booked']:

                guest_name = input("Enter guest name: ")

                self.flight[flight_no]['booked'] = True

                self.flight[flight_no]['guest'] = guest_name

                print(f"\nFlight {flight_no} successfully booked for {guest_name}.")

            else:

                print("\nFlight is either not available or already booked.")

        except ValueError:

            print("\nInvalid flight number. Please enter a valid flight number.")

    def check_flight(self, flight_no):

        guest_name = input("\nEnter guest name to check booking: ")

        found = False

        for flight_no, details in self.flight.items():

            if details['booked'] and details['guest'] == guest_name:

                print(f"\n{guest_name} has booked for {flight_no}: {details['arrival']} - {details['price']}")

                found = True

                break

        if not found:
            print("\nNo flight booking for {guest_name}.")

    def cancel_flight(self, flight_no):

        guest_name = input("\nEnter guest name to cancel: ")

        for flight_no, details in self.flight.items():

            if details['booked'] and details['guest'] == guest_name:

                self.flight[flight_no]['booked'] = False

                self.flight[flight_no]['guest'] = None

                print(f"\nFlight {flight_no} cancelled for {guest_name}.")

                return

            print("\nNo flight booking for {guest_name}.")

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


