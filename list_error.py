# Handling IndexError

numbers = [10, 20, 30]

try:
    index = int(input("Enter index: "))
    print("Value =", numbers[index])

except IndexError:
    print("Error: Index is out of range.")

except ValueError:
    print("Error: Enter a valid number.")

finally:
    print("Program Ended.")