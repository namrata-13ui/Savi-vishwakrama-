# File-Based Notes App

FILE_NAME = "notes.txt"

def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("✅ Note added successfully!")

def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        if not notes:
            print("No notes available.")
        else:
            print("\n----- Your Notes -----")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")

    except FileNotFoundError:
        print("No notes found. Add a note first.")

def main():
    while True:
        print("\n===== Notes App =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Thank you for using Notes App!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()