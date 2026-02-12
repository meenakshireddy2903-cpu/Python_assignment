import logging

logging.basicConfig(
    filename="hostel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class HostelRoom:
    hostel_name = "BVRIT HOSTEL"
    room_rent = 3000   

    def __init__(self, student_name, room_number, months):
        self.student_name = student_name
        self.room_number = room_number
        self.months = months
        self.is_allocated = False
        self.total_fee = 0
    
    def allocate_room(self):
        self.is_allocated = True
        logging.info("Room %s allocated to %s", self.room_number, self.student_name)
    
    def vacate_room(self):
        self.is_allocated = False
        logging.info("Room %s vacated by %s", self.room_number, self.student_name)

    
    def calculate_monthly_fee(self):
        self.total_fee = self.months * HostelRoom.room_rent
        logging.info("Stay months: %s", self.months)
        logging.info("Total fee for %s is %s", self.student_name, self.total_fee)

    
    @classmethod
    def update_room_rent(cls, new_rent):
        cls.room_rent = new_rent
        logging.info("Room rent updated to: %s", cls.room_rent)

room1 = HostelRoom("Meenakshi", 101, 3)

room1.allocate_room()
room1.calculate_monthly_fee()

HostelRoom.update_room_rent(3500)

room1.calculate_monthly_fee()
room1.vacate_room()
