'''#counting charecters in string

def rev_str(text):
    reversed_text =""
    for char in text:
        reversed_text =char+reversed_text
    return reversed_text
    return count
def main():
    text = input("enter name : ")
    print("reversed text: ", rev_str(text))
main()'''

expenses = []

def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

def add_expense():
    name = input("Enter the expense name: ")
    try:
        amount = float(input("Enter amount: "))
        expenses.append({"name": name, "amount": amount})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount! Please enter a number.")

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n----- Expense List -----")
    total = 0

    for expense in expenses:
        print(f"{expense['name']} - ₹{expense['amount']}")
        total += expense['amount']

    print(f"Total Expenses: ₹{total}")

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting.....Thankyou...")
            break
        else:
            print("Invalid choice! Try again.")

main()
        
     
    
