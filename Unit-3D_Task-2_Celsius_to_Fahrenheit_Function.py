# Example solution: Celsius to Fahrenheit (function)
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

celsius = 65
fahrenheit = celsius_to_fahrenheit(celsius)
print("Fahrenheit:", fahrenheit)