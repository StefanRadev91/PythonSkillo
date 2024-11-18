import csv

input_file =  "/Users/stefanradev/Documents/SkilloPython/Homework_lection_9/employee_data.csv" 
output_file = "/Users/stefanradev/Documents/SkilloPython/Homework_lection_9/total_salaries.csv"  

try:
    with open(input_file, mode="r") as infile:
        reader = csv.reader(infile)
        
        output_data = []
        for row in reader:
            if len(row) == 3:  
                name = row[0]
                try:
                    base_salary = float(row[1])
                    bonus = float(row[2])
                    total_salary = base_salary + bonus
                    output_data.append({
                        "Name": name,
                        "Base Salary": base_salary,
                        "Bonus": bonus,
                        "Total Salary": total_salary
                    })
                except ValueError:
                    print(f"Skipping row due to invalid salary or bonus data: {row}")
            else:
                print(f"Skipping invalid row: {row}")

    with open(output_file, mode="w", newline="") as outfile:
        fieldnames = ["Name", "Base Salary", "Bonus", "Total Salary"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        writer.writerows(output_data)

    print(f"Total salaries calculated and saved to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")