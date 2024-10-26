import temperature_conversion

def main():
    temp = float(input("Enter the temperature: "))
    unit = input("Is the temperature in Celsius (C) or Fahrenheit (F)? ").upper()

    if unit == "C":
        print(f"{temp}°C is {temperature_conversion.celsius_to_fahrenheit(temp):.2f}°F")
    elif unit == "F":
        print(f"{temp}°F is {temperature_conversion.fahrenheit_to_celsius(temp):.2f}°C")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()