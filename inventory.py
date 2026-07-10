# Inventory Management

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

print("Inventory")

for item, qty in inventory.items():
    print(item, ":", qty)

# Update Quantity
inventory["Laptop"] += 5

print("\nUpdated Inventory")

for item, qty in inventory.items():
    print(item, ":", qty)