from flight import NationalFlight, InternationalFlight

class FlightManager:
    def __init__(self):
        self.flights = [
            InternationalFlight(101,'Rome', 15000),
            InternationalFlight(102, 'Catania', 25000),
            InternationalFlight(201, 'Paris', 23500),
            InternationalFlight(310, 'London', 35000),
            NationalFlight(501, 'Debrecen', 5000),
            NationalFlight( 502, 'Szeged', 7500)
        ]
        self.bookings = {} #járatszám mappelése a névhez

    def view_available_flights(self):
        print("\nElérhető járatok")
        for flight in self.flights:
            if flight.flight_no not in self.bookings:
                print(f"Járat adatai: {flight}")

#járat foglalása
    def book_flight(self):
        self.view_available_flights()
        try:
            flight_no = int(input("Adja meg a járatszámot: "))
            if flight_no in self.bookings:
                print("Ez a járat már levan foglalva.")
                return
            flight = self.get_flight_by_number(flight_no)
            if flight:
                guest_name = input("Adja meg az utas nevét: ")
                self.bookings[flight_no] = guest_name
                print(f"{flight_no} járat sikeresen lefoglalva {guest_name} néven")
            else:
                print("Nincs ilyen járatszám")
        except ValueError:
            print("\nHibás járatszám. Adjon meg egy helyes járatszámot")

#járat ellenőrzése
    def check_flight(self):
        guest_name = input("\nAdja meg az utas nevét az ellenőrzéshez: ")
        for flight_no, name in self.bookings.items():
            if name == guest_name:
                flight = self.get_flight_by_number(flight_no)
                print(f"{guest_name} foglalt a(z) {flight}")
                return
        print("Nincs foglalás ezen a néven.")

#járat törllése
    def cancel_flight(self):
        guest_name = input("\nAdja meg a nevét a törléshez: ")
        for flight_no, name in list(self.bookings.items()):
            if name == guest_name:
                del self.bookings[flight_no]
                print(f"A(z) {flight_no} járat törölve lett {guest_name} részére.")
                return
        print("Nincs foglalás ezen a néven.")

    def get_flight_by_number(self, flight_no):
        for flight in self.flights:
            if flight.flight_no == flight_no:
                return flight
        return None