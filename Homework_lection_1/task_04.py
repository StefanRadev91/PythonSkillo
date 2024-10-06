# Write a program that converts temperatures from Fahrenheit to Celsius. 
# Prompt the user to enter a temperature in Fahrenheit and then print out the equivalent
# temperature in Celsius.

temperature_in_Fahrenheit = int(input("Please enter temperateure in Fahrenheit to convert in Celsius: "))

converted_in_Celsius_temperature = (5 / 9) * (temperature_in_Fahrenheit - 32)

print(converted_in_Celsius_temperature)