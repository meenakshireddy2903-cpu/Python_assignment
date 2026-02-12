import logging

logging.basicConfig(
    filename="ticket.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Ticket:
    railway_name = "South Central Railway"
    base_fare = 100   

    def __init__(self, passenger_name, distance):
        self.passenger_name = passenger_name
        self.distance = distance
        self.ticket_booked = False
        self.total_fare = 0

    
    def book_ticket(self):
        self.ticket_booked = True
        logging.info("Ticket booked for %s", self.passenger_name)

    
    def cancel_ticket(self):
        self.ticket_booked = False
        logging.info("Ticket cancelled for %s", self.passenger_name)

    
    def calculate_fare(self):
        self.total_fare = self.distance * Ticket.base_fare
        logging.info("Travel distance: %s km", self.distance)
        logging.info("Total fare for %s is %s", self.passenger_name, self.total_fare)

    
    @classmethod
    def update_base_fare(cls, new_fare):
        cls.base_fare = new_fare
        logging.info("Base fare updated to: %s", cls.base_fare)
ticket1 = Ticket("Meenakshi", 495)

ticket1.book_ticket()
ticket1.calculate_fare()

Ticket.update_base_fare(120)

ticket1.calculate_fare()
ticket1.cancel_ticket()
