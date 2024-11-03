# Problem 8:
# Design a class "Employee" with encapsulated attributes for name and salary. 
# Implement a subclass "Manager" that inherits from "Employee" and includes an additional
# attribute for the department.

class Employee:
    def __init__(self, name: str, salary: str):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

class Manager(Employee):
    def __init__(self, name: str, salary: str, department: str):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"{self.name}, {self.salary}, {self.department}"

employee1 = Manager("John McGuinn", "4000 BGN", "Software Development")
print(employee1)

