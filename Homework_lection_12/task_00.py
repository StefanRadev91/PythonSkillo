# Problem 0: Choose a public API of your choice (see https://github.com/public-apis/public-apis).
# - Write a Python program that makes a GET request to the chosen API.
# - Retrieve data from the API and display specific information from the response.
# - Ensure error handling for cases where the request may fail.

import requests

def get_joke():
    url = 'https://v2.jokeapi.dev/joke/Any?type=single'
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        
        data = response.json()
        if 'joke' in data:
            print(f'Joke: {data["joke"]}')
        elif 'setup' in data and 'delivery' in data:
            print(f'{data["setup"]} - {data["delivery"]}')
        else:
            print('Error: Unable to retrieve a joke.')
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')

if __name__ == '__main__':
    get_joke()