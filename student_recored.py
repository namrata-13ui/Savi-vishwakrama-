# Student Record Management

students = {
    "101": {"Name": "Rahul", "Age": 20, "Marks": 88},
    "102": {"Name": "Priya", "Age": 19, "Marks": 92},
    "103": {"Name": "Aman", "Age": 21, "Marks": 85}
}

print("Student Records\n")

for roll, details in students.items():
    print(f"Roll No: {roll}")
    for key, value in details.items():
        print(f"{key}: {value}")
    print()

# Update Marks
students["101"]["Marks"] = 90

print("Updated Record:")
print(students["101"])