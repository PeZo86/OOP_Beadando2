
from flight import NationalFlight, InternationalFlight, FlightCompany

class FlightManager:
    def __init__(self):
        #Légitársaság létrehozása:
        self.wizzair = FlightCompany("Wizzair")
        self.ryanair = FlightCompany("Ryanair")
        self.britishair = FlightCompany("BritishAir")
        self.malev = FlightCompany("Malév")

        #Járat a WizzAir-hez
        self.wizzair.add_flight(InternationalFlight(101, "Rome", 15000, self.wizzair))
        self.wizzair.add_flight(InternationalFlight(102, "Catania", 35000, self.wizzair))
        self.wizzair.add_flight(InternationalFlight(103, "Madrid", 40000, self.wizzair))

        #Járat a Ryanair-hez
        self.ryanair.add_flight(InternationalFlight(201, "Paris", 37000, self.ryanair))
        self.ryanair.add_flight(InternationalFlight(202, "Barcelona", 40000, self.ryanair))
        self.ryanair.add_flight(InternationalFlight(203, "Berlin", 40000, self.ryanair))

        #Járat a BritishAir-hez
        self.britishair.add_flight(InternationalFlight(301, "London", 50000, self.britishair))
        self.britishair.add_flight(InternationalFlight(302, "Leeds", 70000, self.britishair))

        #Járat a Malév-hez
        self.malev.add_flight(NationalFlight(506, "Debrecen", 3000, self.malev))
        self.malev.add_flight(NationalFlight(507, "Szeged", 4000, self.malev))

        #Járatok tárolása listában
        self.companies = [self.wizzair, self.ryanair, self.britishair, self.malev]

        self.bookings = {}

    def get_all_flights(self):
        all_flights = []
        for company in self.companies:
            all_flights.extend(company.flights)
        return all_flights

    def view_available_flights(self):
        print("\nElérhető járatok")
        for flight in self.get_all_flights():
            if flight.flight_no not in self.bookings:
                print(f"Járat adatai: {flight}")

    # járat szerinti megjelenítés
    def get_company_by_name(self, name):
        for company in self.companies:
            if company.name.lower() == name.lower():
                return company
        return None

    def view_filghts_by_company(self):
        print("\nElérhető légitársaságok: ")
        for company in self.companies:
            print(f" - {company.name}")

        company_name = input("Adja meg a légitársaság nevét: ")
        company = self.get_company_by_name(company_name)

        if company:
            flights = company.flights
            print(f"\n{company.name} járatai: ")
            if not flights:
                print("Nincsennek elérhető járatok ennél a légitársaságnál")
            else:
                for flight in flights:
                    if flight.flight_no not in self.bookings:
                        print(f" {flight}")
        else:
            print("Nincs ilyen nevű légitársaság")

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


#foglalás ellenőrzése
    def check_flight(self):
        guest_name = input("\nAdja meg az utas nevét az ellenőrzéshez: ")
        for flight_no, name in self.bookings.items():
            if name == guest_name:
                flight = self.get_flight_by_number(flight_no)
                print(f"{guest_name} foglalt a(z) {flight}")
                return
        print("Nincs foglalás ezen a néven.")


#foglalás törlése
    def cancel_flight(self):
        guest_name = input("\nAdja meg a nevét a törléshez: ")
        for flight_no, name in list(self.bookings.items()):
            if name == guest_name:
                del self.bookings[flight_no]

                print(f"A(z) {flight_no} járat törölve lett {guest_name} nevéről.")
                return
        print("Nincs foglalás ezen a néven.")

    def get_flight_by_number(self, flight_no):
        for flight in self.get_all_flights():
            if flight.flight_no == flight_no:
                return flight
        return None
