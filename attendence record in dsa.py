attendance = {}

def show_menu():
    print("\nAttendance Tracker")
    print("1. Add attendance")
    print("2. Show attendance")
    print("3. Exit")

def add_attendance():
    name = input("Enter the name: ")
    status = input("Enter status (Present/Absent): ").capitalize()
    attendance[name] = status
    print("Attendance added successfully.")

def view_attendance():
    if not attendance:
        print("No attendance records found.")
    else:
        print("-------- Attendance Records --------")
        for name, status in attendance.items():
            print(f"{name} - {status}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main()
