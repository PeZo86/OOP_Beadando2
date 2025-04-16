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

#öröklik a járat osztályt és megvalósítják a járat típust
class NationalFlight(Flight):

    def flight_type(self):
        return "Belföldi"

class InternationalFlight(Flight):

    def flight_type(self):
        return "Nemzetközi"

# tárolja a járatokat és azok nevét
class FlightCompany:

    def __init__(self, nev):
        self.nev = nev
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def total_flight(self):
        return self.flights

    def __repr__(self):
        return f"Légi társaság: {self.nev}, Járat száma: {len(self.flights)}"

from functions import Flight

    def main():
        flight_manager = Flight()

        while True:
            print("\nÜdvözlöm a Simple Booking App-ban")
            print("1. Mutasd az elérhető járatokat")
            print("2. Járat foglalása")
            print("3. Járat ellenőrzése")
            print("4. Járat törlése")
            print("5. Kilépés")

            try:
                choice = int(input("Adja meg mit szeretne: "))
                if choice == 1:
                    self.view_available_flights()
                elif choice == 2:
                    self.book_flight()
                elif choice == 3:
                    self.check_flight()
                elif choice == 4:
                    self.cancel_flight()
                elif choice == 5:
                    print("\nKöszönjük hogy a Simple Booking App-ot használta. Viszlát")
                    break
                else:
                    print("\nHbiás választás. Kérem válasszon egy helyes számot")

            except ValueError:
                print("\nHibás szám. Kérem válasszon 1 és 5 között egy számot")

if __name__ == '__main__':
    main()


