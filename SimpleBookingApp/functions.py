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