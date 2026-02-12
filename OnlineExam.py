import logging
logging.basicConfig(
    filename="exam.log",
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s -%(message)s"
)

class Exam:
    minimum_score = 35
    platform_name = "TopBrains"
    def __init__(self,name,total_marks,_scored_marks):
        self.name = name
        self.total_marks = total_marks
        self.scored_marks = _scored_marks
        self.is_started = False
        self.is_submitted = False
    def start_exam(self):
        self.is_started = True
        logging.info("The exam is started by: %s",self.name)
    def submit_exam(self):
        self.is_submitted = True
        logging.info("The exam is submitted by: %s", self.name)
    def calculate_score(self):
        logging.info("Marks scored: %s",self.scored_marks)
        if self.scored_marks >= Exam.minimum_score:
            logging.info("Passed %s")
        else:
            logging.warning("Failed %s")
    @classmethod
    def update_pass_marks(cls, new_pass_marks):
        cls.pass_marks = new_pass_marks
        logging.info("Minimum_score updated to: %s", cls.minimum_score)

student1 = Exam("Meenakshi", 100, 30)

student1.start_exam()
student1.submit_exam()
student1.calculate_score()

Exam.update_pass_marks(50)

student1.calculate_score()
