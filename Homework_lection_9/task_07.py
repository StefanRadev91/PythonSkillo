import csv
import json

file_path = "/Users/stefanradev/Documents/SkilloPython/Homework_lection_9/student_data.csv"

def calculate_averages(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            print("Average Scores:")
            for row in reader:
                name = row["name"]
                scores = json.loads(row["scores"])  
                average = sum(scores) / len(scores)
                print(f"  {name}: {average:.2f}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: JSON data in the file is not properly formatted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculate_averages(file_path)