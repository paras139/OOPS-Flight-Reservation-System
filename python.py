class Flight:
    def __init__(self,flight_number,destination,seats_available):
        self.flight_number=flight_number
        self.destination=destination
        self.seats_available=seats_available
        self.passengers=[]

    def display_flight_info(self):
        print(f'Flight Number is :{self.flight_number}, destination:{self.destination}, Seats available: {self.seats_available}')

    def book_ticket(self,passenger):
        if self.seats_available>0:
            self.seats_available-=1
            self.passengers.append(passenger)
            passenger.ticket_number=f'{self.flight_number}--{len(self.passengers)}'
            print(f'{passenger.name},Ticket booked successfully! Ticket Number: {passenger.ticket_number}')
        else:
            print(f'Sorry, flight {self.flight_number} to {self.destination} is fully booked.')
    
    def display_passenger_list(self):
        if not self.passengers:
            print(f'No passenger is {self.flight_number}')
        else: 
         print(f'Passenger in {self.flight_number}')
         for i in self.passengers:
             print(f'{i.name}: {i.ticket_number}')

class Passenger():
    def __init__(self,name):
        self.name=name
        self.ticket_number=None
    def __str__(self):
        return f'Passenger name:{self.name}, {self.ticket_number if self.ticket_number else "Not booked"}'
    
class FlightReservationSystem:
    def __init__(self):
        self.flights=[]
    def add_flight(self,flight):
        self.flights.append(flight)
        print(f'Flight {flight.flight_number} to destination {flight.destination}')
    def view_avilable_flights(self):
        print('All flights are given below')
        for i in self.flights:
            i.display_flight_info()
    def find_flight(self,flight_number):
        for i in self.flights:
            if flight_number==i.flight_number:
                return i
        return None
if __name__=='__main__':
    systems=FlightReservationSystem()
    f1=Flight('P239','Mumbai',99)
    f2=Flight('B199','Bangalore',88)
    systems.add_flight(f1)
    systems.add_flight(f2)
    systems.view_avilable_flights()
    p1=Passenger('Paras')
    p2=Passenger('Som')
    selected_flight=systems.find_flight('P239')
    if selected_flight:
        selected_flight.book_ticket(p1)
        selected_flight.book_ticket(p2)
    if selected_flight:
        selected_flight.display_passenger_list()
        systems.view_avilable_flights()
 
