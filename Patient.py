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




