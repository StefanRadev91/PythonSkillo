import xml.etree.ElementTree as ET

def read_inventory(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        print("Course List:")
        for product in root.findall("product"):
            name = product.find("name").text
            price = product.find("price").text
            print(f"  Course: {name}, Price: ${price}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except ET.ParseError:
        print(f"Error: The file '{file_path}' contains invalid XML.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_path = "/Users/stefanradev/Documents/SkilloPython/Homework_lection_9/inventory.xml"
    read_inventory(file_path)