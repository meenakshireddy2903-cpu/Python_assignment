import logging

logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Employee:
    company_name = "Goldmansachs"
    hra_percentage = 10  

    def __init__(self, emp_name, basic_sal, leave_days):
        self.emp_name = emp_name
        self.basic_sal = basic_sal
        self.leave_days = leave_days
        self.final_sal = basic_sal

    def calculate_salary(self):
        hra_amount = (self.basic_sal * Employee.hra_percentage) / 100
        self.final_sal = self.basic_sal + hra_amount
        logging.info("Salary after adding HRA for %s is %s", self.emp_name, self.final_sal)


    def apply_leave_deduction(self):
        deduction_per_day = 500
        total_deduction = self.leave_days * deduction_per_day
        self.final_sal = self.final_sal - total_deduction
        logging.info("Leave deduction for %s is %s", self.emp_name, total_deduction)

    def display_payslip(self):
        logging.info("Employee Name: %s", self.emp_name)
        logging.info("Basic Salary: %s", self.basic_sal)
        logging.info("Final Salary: %s", self.final_sal)


    @classmethod
    def update_hra_percentage(cls, new_hra):
        cls.hra_percentage = new_hra
        logging.info("HRA percentage updated to: %s", cls.hra_percentage)

emp1 = Employee("Meenakshi", 30000, 2)

emp1.calculate_salary()
emp1.apply_leave_deduction()
emp1.display_payslip()

Employee.update_hra_percentage(15)

emp1.calculate_salary()
emp1.display_payslip()
