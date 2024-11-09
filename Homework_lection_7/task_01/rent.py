class Rent:
    def __init__(self, amount, due_date):
        self.amount = amount
        self.due_date = due_date
        self.status = "overdue"

    def record_payment(self):
        self.status = "paid"
        print(f"Payment of {self.amount} made on due date {self.due_date}")

    def check_payment_status(self):
        return self.status



