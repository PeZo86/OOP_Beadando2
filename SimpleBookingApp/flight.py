from abc import ABC, abstractmethod

class Flight(ABC):

    def __init__(self, flight_no, arrival, price, company):
        self.flight_no = flight_no
        self.arrival = arrival
        self.price = price
        self.company = company


    def flight_type(self):
        pass


    def flight_company(self):
        return self.company.name if self.company else "N/A"

    def __repr__(self):
        return (f"{self.flight_type()} Járat, "
                f"{self.flight_company()} | "
                f"Járatszám: {self.flight_no} -> Érkezés: {self.arrival} "
                f"Ár: {self.price} Ft")


#öröklik a járat osztályt és megvalósítják a járat típust
class NationalFlight(Flight):
    def flight_type(self):
        return "Belföldi"

class InternationalFlight(Flight):
    def flight_type(self):
        return "Nemzetközi"

# tárolja a légitársaságokat és azok nevét
class FlightCompany:
    def __init__(self, nev):
        self.nev = nev
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def total_flight(self):
        return self.flights

    def __repr__(self):
        result = f"\nLégi társaság: {self.name} ({len(self.flights)} járat)\n"
        for flight in self.flights:
            result += f" {flight}\n"
        return result
