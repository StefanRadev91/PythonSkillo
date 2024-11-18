import csv
import os

def main():
    directory = "/Users/stefanradev/Documents/SkilloPython/Homework_lection_9/"
    os.makedirs(directory, exist_ok=True)  
    file_name = os.path.join(directory, "student_scores.csv")
    
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        file.seek(0, 2) 
        if file.tell() == 0:
            writer.writerow(["Name", "Score"])
        
        print("Enter student names and scores. Type 'exit' to finish.")
        
        while True:
            name = input("Enter student name: ").strip()
            if name.lower() == 'exit':
                print("Data entry finished.")
                break
            try:
                score = float(input(f"Enter score for {name}: ").strip())
                writer.writerow([name, score])
                print(f"Data for {name} saved.")
            except ValueError:
                print("Invalid score. Please enter a numeric value.")

if __name__ == "__main__":
    main()