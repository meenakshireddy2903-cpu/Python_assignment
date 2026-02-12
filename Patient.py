class Patient:
    consultation_fee = 500
    Hospital_name = "Apollo"
    Location = "Hyderabad"

    def __init__(self, name, age, cause, days_in_hospital):
        self.name = name
        self.age = age
        self.cause = cause
        self.days_in_hospital = days_in_hospital
        self.is_in_hospital = False
    def admit_patient(self):
        self.is_in_hospital = True
        print(self.name, "is admitted in Hospital")
    def discharge_patient(self):
        self.is_in_hospital = False
        print(self.name, "is discharged from hospital")
    def calculate_bill(self):
        cost_per_day = 100
        total_bill = (self.days_in_hospital * cost_per_day) + Patient.consultation_fee
        print(self.name, "total bill is:", total_bill)
    @classmethod
    def update_consultation_fee(cls,updated_fee):
        cls.consultation_fee = updated_fee
        print("Update Consultation Fee",cls.consultation_fee)
patient1 = Patient("Meens", 20, "Fever", 3)
patient1.admit_patient()
patient1.discharge_patient()
patient1.calculate_bill()
Patient.update_consultation_fee(700)
patient1.calculate_bill()




"""
import logging
logging.basicConfig(
    filename="library.log",
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s -%(message)s"
)

class LibraryBook:
    library_name = "Central Library"
    library_loc = "Hyderabad"
    fine_per_day = 10   

    def __init__(self, book_name, book_author, submission_delay):
        self.book_name = book_name
        self.book_author = book_author
        self.submission_delay = submission_delay
        self.is_issued = False

    def issue_book(self):
        self.is_issued = True
        logging.info("Book Issued : %s", self.book_name)

    def return_book(self):
        self.is_issued = False
        logging.info("Book Returned: %s",self.book_name)

    def calculate_fine(self):
        total_fine = self.submission_delay * LibraryBook.fine_per_day
        logging.info("Total fine for %s is: %s", self.book_name, total_fine)
    @classmethod
    def update_fine_per_day(cls, latest_fine):
        cls.fine_per_day = latest_fine
        logging.info("Fine per day updated to: %s", cls.fine_per_day)

book1 = LibraryBook("Python", "Aditya", 5)

book1.issue_book()
book1.calculate_fine()
book1.return_book()

LibraryBook.update_fine_per_day(20)

book1.calculate_fine()
"""