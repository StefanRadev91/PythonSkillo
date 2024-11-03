# Problem 9:
# Create a class called "Employee" that has attributes name, start_date, 
# PIN, phone, address, manager_name, department. Implement methods to calculate employee tenure,
# and business card info representation.

from datetime import datetime

class Employee:
    def __init__(self, name, start_date, PIN, phone, address, manager_name, department):
        self.name = name
        self.start_date = start_date
        self.pin = PIN
        self.phone = phone
        self.address = address
        self.manager_name = manager_name
        self.department = department

    def calculate_tenure(self, start_date_str):
        start_date = datetime.strptime(start_date_str, '%d.%m.%Y')
        today = datetime.today()
        tenure_days = (today - start_date).days
        years = tenure_days // 365
        months = (tenure_days % 365) // 30
        days = (tenure_days % 365) % 30
        return f"years: {years}, months: {months}, days: {days}"
     
    def __str__(self):
        return f"Employee Name: {self.name}, Start Date: {self.start_date}, PIN: {self.pin}, Phone: {self.phone}, Address: {self.address}, Manager Name: {self.manager_name}, Department: {self.department}"
    
employee1 = Employee("Stefan Radev", "27.11.2023", 7110017733, "0897268135", "Sofia", "Yancho", "Quality Assurance")

print(employee1)
print(employee1.calculate_tenure("27.11.2023"))