# Week 4 Task 3
# Debugged Python Script

try:
    numbers = [10, 20, 30, 40]

    index = int(input("Enter list index (0-3): "))

    print("Value:", numbers[index])

except ValueError:
    print("Invalid input! Please enter an integer.")

except IndexError:
    print("Index out of range!")

finally:
    print("Debugging example finished.")