
students_accounts = {}

students_accounts["John"] = [123456]
students_accounts["Jason"] = [1234567899]

new_account = 789012

if "John" in students_accounts:
    students_accounts["John"].append(new_account)
else:
    students_accounts["John"] = [new_account]

for student, accounts in students_accounts.items():
    print(student, accounts)
