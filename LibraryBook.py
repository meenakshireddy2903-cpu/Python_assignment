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

