class Apartment:
    def __init__(self, apartment_number, square_footage, rent_amount):
        self.apartment_number = apartment_number
        self.square_footage = square_footage
        self.rent_amount = rent_amount

    def display_apartment_details(self):
        print(f"Apartment Number: {self.apartment_number}")
        print(f"Square Footage: {self.square_footage}")
        print(f"Rent Amount: {self.rent_amount}")