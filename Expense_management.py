print("******Assalamu Alaikum*******")
print("*****Welcome to Expense Manager*****")

# List to store history
history = []
balance = 0.0

# Main menu
while True:
    print("\nMenu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transaction History")
    print("5. View Income Report")
    print("6. View Expense Report")
    print("7. Exit")
    
    # Taking user input for the menu
    choice = input("Please choose an option (1-7): ")
    
    if choice == '1':
        # Add Income
        income_category = input("Please enter income category: ")
        income = float(input("Enter income: "))
        balance += income
        history.append(f"Income: {income_category} - {income}")
        print(f"Income of {income} added under category: {income_category}")
    
    elif choice == '2':
        # Add Expense
        expense_category = input("Please enter expense category: ")
        expense = float(input("Enter expense: "))
        balance -= expense
        history.append(f"Expense: {expense_category} - {expense}")
        print(f"Expense of {expense} added under category: {expense_category}")
    
    elif choice == '3':
        # View Balance
        print(f"\nYour current balance is: {balance}")
    
    elif choice == '4':
        # View Transaction History
        print("\nTransaction History:")
        if not history:
            print("No transactions yet.")
        else:
            for record in history:
                print(record)
    
    elif choice == '5':
        # View Income Report
        print("\nIncome Report:")
        income_found = False
        for record in history:
            if "Income" in record:
                print(record)
                income_found = True
        if not income_found:
            print("No income recorded yet.")
    
    elif choice == '6':
        # View Expense Report
        print("\nExpense Report:")
        expense_found = False
        for record in history:
            if "Expense" in record:
                print(record)
                expense_found = True
        if not expense_found:
            print("No expenses recorded yet.")
    
    elif choice == '7':
        # Exit the program
        print("Thank you for using Expense Manager. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please choose a valid option (1-7).")
        