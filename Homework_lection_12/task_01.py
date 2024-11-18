import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

GEO_API_KEY = "r8AH4yxphCr5pcajrMQn8OUHIwUIYuHNpUfYOwzH"

def fetch_city_coordinates(city):
    url = f"https://api.api-ninjas.com/v1/geocoding?city={city}"
    headers = {"X-Api-Key": GEO_API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200 and response.json():
        location = response.json()[0]  
        return location['latitude'], location['longitude']
    else:
        print(f"Error: Could not find coordinates for {city}.")
        return None, None

def fetch_weather_data(latitude, longitude, date):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&start_date={date}&end_date={date}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching weather data.")
        return None

    data = response.json()
    if 'hourly' not in data:
        print("No hourly data found in the response.")
        return None

    times = data['hourly']['time']
    temperatures = data['hourly']['temperature_2m']

    df = pd.DataFrame({
        'time': pd.to_datetime(times),
        'temperature': temperatures
    })

    return df

def plot_temperature_forecast(city, date, df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=df['time'], y=df['temperature'], marker='o', color='b')
    plt.title(f"Temperature Forecast for {city} on {date}")
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    city = input("Enter the name of the city: ")
    date = input("Enter the date for the forecast (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Incorrect date format. Please use YYYY-MM-DD.")
        return

    latitude, longitude = fetch_city_coordinates(city)
    if latitude is None or longitude is None:
        print("Cannot fetch weather data without valid coordinates.")
        return
    
    weather_data = fetch_weather_data(latitude, longitude, date)
    if weather_data is not None:
        plot_temperature_forecast(city, date, weather_data)

if __name__ == "__main__":
    main()