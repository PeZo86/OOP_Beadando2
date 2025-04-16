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
        print("\nElérhető járatok")

        for flight_no, details in self.flight.keys():

            if not details['booked']:
                print(f"Járat adatai: {flight_no}: {details['arrival']} - {details['price']}")

    def book_flight(self, flight_no):
        self.view_available_flights()
        try:
            flight_no = int(input("Enter flight no: "))
            if flight_no in self.flight.keys() and not self.flight[flight_no]['booked']:
                guest_name = input("Enter guest name: ")
                self.flight[flight_no]['booked'] = True
                self.flight[flight_no]['guest'] = guest_name
                print(f"\nA járat {flight_no} sikeresen lefoglalva az alábbi néven: {guest_name}.")

            else:
                print("\nA járat nem elérhető vagy már le lett foglalva.")

        except ValueError:
            print("\nHibás járatszám. Adjon meg egy érvényes járatszámot")

    def check_flight(self, flight_no):
        guest_name = input("\nAdja meg a neve a járat ellenőrzéséhez ")
        found = False
        for flight_no, details in self.flight.items():
            if details['booked'] and details['guest'] == guest_name:
                print(f"\n{guest_name} foglalt az alábbi járatra {flight_no}: {details['arrival']} - {details['price']}")
                found = True
                break

        if not found:
            print("\nNincs foglalás az alábbi néven {guest_name}.")

    def cancel_flight(self, flight_no):
        guest_name = input("\nAdja meg a nevet a törléshez: ")
        for flight_no, details in self.flight.items():
            if details['booked'] and details['guest'] == guest_name:
                self.flight[flight_no]['booked'] = False
                self.flight[flight_no]['guest'] = None
                print(f"\nAz alábbi járat {flight_no} törölve lett az alábbi utas nevéről {guest_name}.")
                return

            print("\nNincs foglalás az alábbi néven {guest_name}.")