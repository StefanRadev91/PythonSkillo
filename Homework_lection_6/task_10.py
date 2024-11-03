# Problem 10:
# Create an abstract class "Employee" with attributes for name and salary. Implement a subclass "Manager" 
# that inherits from "Employee" and includes an additional
# attribute for the department. Ensure that the "Employee" class enforces 
# encapsulation. 
# Every employee and manager should have a method to send a message to. The
# message must be stored. Create a class "Team" that has a manager and a 
# list of members. Implement a method that sends a message to everyone in the team.

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, salary: float):
        self.__name = name
        self.__salary = salary
        self.__messages = []

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    def send_message(self, message: str):
        if not message:
            raise ValueError("Message cannot be empty.")
        self.__messages.append(message)
        print(f"{self.__name} received message: {message}")

    def get_messages(self):
        return self.__messages

    @abstractmethod
    def get_info(self):
        pass


class SimpleEmployee(Employee):
    def get_info(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

    def __str__(self):
        return self.get_info()


class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.__department = department  

    @property
    def department(self):
        return self.__department

    def get_info(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"

    def __str__(self):
        return self.get_info()


class Team:
    def __init__(self, manager: Manager):
        self.manager = manager
        self.members = []

    def add_member(self, employee: Employee):
        self.members.append(employee)

    def send_message_to_team(self, message: str):
        self.manager.send_message(message)
        for member in self.members:
            member.send_message(message)


def test_team_communication():
    manager = Manager("Stefan Radev", 4000, "Software Development")

    team = Team(manager)

    employee1 = SimpleEmployee("Nikola", 2000)
    employee2 = SimpleEmployee("Sofiya", 2300)

    team.add_member(employee1)
    team.add_member(employee2)

    message = "Meeting at 10 AM tomorrow."
    team.send_message_to_team(message)

    assert message in manager.get_messages(), "Manager did not receive the message."
    assert message in employee1.get_messages(), "Employee 1 did not receive the message."
    assert message in employee2.get_messages(), "Employee 2 did not receive the message."

    print("All tests passed!")

test_team_communication()