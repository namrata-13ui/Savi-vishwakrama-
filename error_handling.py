# Week 4 Task 3
# Error Handling using try-except

def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Error: Please enter valid numeric values.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    else:
        print("Result:", result)

    finally:
        print("Program execution completed.")


divide_numbers()