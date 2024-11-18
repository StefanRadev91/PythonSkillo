import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    if response.text.strip():
        try:
            data = response.json()
            file_path = '/Users/stefanradev/Documents/SkilloPython/Homework_lection_11/response.json'
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"JSON data successfully written to {file_path}")
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON. Raw response:", response.text)
    else:
        print("Empty response received.")
else:
    print(f"Request failed with status code: {response.status_code}")