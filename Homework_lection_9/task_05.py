import json

def calculate_total_cost(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("The JSON data must be a list of products.")

            total_cost = 0

            for product in data:
                if 'price' in product:
                    total_cost += product['price']
                else:
                    raise ValueError(f"Product {product.get('name', 'Unnamed')} is missing a price.")

            print(f"Total cost of all products: ${total_cost:.2f}")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON file.")
    except Exception as e:
        print(f"Error: {e}")

filename = '/Users/stefanradev/Documents/SkilloPython/Homework_lection_9/products.json'
calculate_total_cost(filename)