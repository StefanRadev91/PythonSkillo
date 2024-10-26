# Create a Python program that simulates an online shopping cart using a global dictionary variable. 
# Every customer has unique id as a key. Define functions to add items to the cart, remove items, calculate the total price, and
# display the contents of the cart. Allow the user to interact with the cart by adding and removing items.

shopping_carts = {}

def add_item(customer_id, item_name, item_price):
    if customer_id not in shopping_carts:
        shopping_carts[customer_id] = []
    
    shopping_carts[customer_id].append((item_name, item_price))
    print(f"Added {item_name} to customer {customer_id}'s cart.")

def remove_item(customer_id, item_name):
    if customer_id in shopping_carts:
        cart = shopping_carts[customer_id]
        for item in cart:
            if item[0] == item_name:
                cart.remove(item)
                print(f"Removed {item_name} from customer {customer_id}'s cart.")
                return
    print(f"{item_name} not found in customer {customer_id}'s cart.")

def calculate_total(customer_id):
    if customer_id in shopping_carts:
        total = sum(item[1] for item in shopping_carts[customer_id])
        return total
    return 0.0

def display_cart(customer_id):
    if customer_id in shopping_carts:
        print(f"Customer {customer_id}'s cart:")
        for item in shopping_carts[customer_id]:
            print(f" - {item[0]}: ${item[1]:.2f}")
    else:
        print(f"Customer {customer_id} has an empty cart.")

def main():
    while True:
        print("\n--- Online Shopping Cart ---")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Calculate total price")
        print("4. Display cart contents")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            customer_id = input("Enter customer ID: ")
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            add_item(customer_id, item_name, item_price)

        elif choice == '2':
            customer_id = input("Enter customer ID: ")
            item_name = input("Enter item name to remove: ")
            remove_item(customer_id, item_name)

        elif choice == '3':
            customer_id = input("Enter customer ID: ")
            total = calculate_total(customer_id)
            print(f"Total price for customer {customer_id}: ${total:.2f}")

        elif choice == '4':
            customer_id = input("Enter customer ID: ")
            display_cart(customer_id)

        elif choice == '5':
            print("Exiting the shopping cart simulation.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()