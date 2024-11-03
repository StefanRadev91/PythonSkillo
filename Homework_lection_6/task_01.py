# Problem 1:
# instances.
# Define a class "Email" with special methods 
# "__eq__" and "__ne__" to compare two email addresses. Test the equality and inequality operators with different email

class Email:
    def __init__(self, mail):
        self.mail = mail
        
    def __eq__(self, other_email):
        if isinstance(other_email, Email):
            return self.mail == other_email.mail
        return False  

    def __ne__(self, other_email):
        return not self == other_email

email1 = Email("drak0@abv.bg")
email2 = Email("drak0@abv.bg")

print(email1 == email2) 
print(email1 != email2)