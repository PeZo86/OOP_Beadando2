from abc import ABC, abstractmethod
2
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