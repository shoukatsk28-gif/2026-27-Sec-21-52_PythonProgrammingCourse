try:
    a = int("10")
    b = int("2")
    result = a / b
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter valid numbers.")
else:
    print("Result:", result) 
finally:
    print("Program finished.") 