# Simple Contact Book

contacts = {
    "Rahul": "9876543210",
    "Priya": "8765432109",
    "Aman": "7654321098"
}

print("Contact Book")

for name, number in contacts.items():
    print(name, ":", number)

# Add New Contact
contacts["Riya"] = "9123456780"

print("\nAfter Adding Contact:")
for name, number in contacts.items():
    print(name, ":", number)

# Search Contact
search = input("\nEnter name to search: ")

if search in contacts:
    print("Phone Number:", contacts[search])
else:
    print("Contact not found.")