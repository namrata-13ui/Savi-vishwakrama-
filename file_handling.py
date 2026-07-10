# Handling FileNotFoundError

try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File does not exist.")

finally:
    print("File operation completed.")