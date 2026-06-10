class NoteManager:
    def __init__(self, filename):
        self.filename = filename

    def add_note(self):
        note = input("Enter note: ")
        with open(self.filename, "a") as file:  
            file.write(note + "\n")
        print("Note added successfully!")

    def view_notes(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()
            if data == "":
                print("No notes available.")
            else:
                print("\n----- NOTES -----")
                print(data)
        except FileNotFoundError:
            print("No notes file found.")

    def search_note(self):
        keyword = input("Enter keyword: ")

        try:
            with open(self.filename, "r") as file:
                found = False
                for line in file:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True
                if not found:
                    print("Note not found.")
        except FileNotFoundError:
            print("No notes file found.")

    def delete_all_notes(self):
        choice = input("Delete all notes? (yes/no): ")

        if choice.lower() == "yes":
            with open(self.filename, "w") as file:
                file.write("")
            print("All notes deleted.")
        elif choice.lower() == "no":
            print("Deletion cancelled.")
        else:
            print("Invalid choice.")

manager = NoteManager("notes.txt")

while True:
    try:
        print("\n===== NOTES MANAGEMENT SYSTEM =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Note")
        print("4. Delete All Notes")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            manager.add_note()
        elif choice == "2":
            manager.view_notes()
        elif choice == "3":
            manager.search_note()
        elif choice == "4":
            manager.delete_all_notes()
        elif choice == "5":
            print("Thank You")
            break
        else:
            print("Invalid choice")
    except Exception as e:
        print("Unexpected Error:", e)