import json

file_path = "/Users/stefanradev/Documents/SkilloPython/Homework_lection_9/contacts.json"

def read_contacts(file_path):
    try:
        with open(file_path, 'r') as file:
            contacts = json.load(file)

        print("Contact Information:")
        for index, contact in enumerate(contacts, start=1):
            print(f"\nContact {index}:")
            print(f"  Name:  {contact.get('name', 'N/A')}")
            print(f"  Email: {contact.get('email', 'N/A')}")
            print(f"  Phone: {contact.get('phone', 'N/A')}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_contacts(file_path)