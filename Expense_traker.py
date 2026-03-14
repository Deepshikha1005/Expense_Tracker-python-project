# Expense Tracker project (calculating the expenses for my friend's birthday)
expense_List = []  # List of expenses
monthly_budget = float(input("Enter your monthly pocket money: "))
print("Welcome to Expense Tracker! This cost 90% of my monthly pocket money in only one day.")

while True:
    print("\n1: Add Expense")
    print("2: View All Expenses")
    print("3: View Total Expenses")
    print("4: View Total Expenses by Category")
    print("5: View Expense by Date")
    print("6: Exit")
    choice = int(input("Please Enter your choice: "))

    # Add Expense
    if choice == 1:
        date = input("Enter Date (DD/MM/YYYY): ")
        category = input("What did you spend money on: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }
        expense_List.append(expense)
        print("\nDone! Expense added successfully.")

        # High expense alert
        percentage = (amount / monthly_budget) * 100
        if percentage >= 50:
            print("High expense alert!!!! This is more than 50% of your monthly pocket karch")

    # View All Expenses
    elif choice == 2:
        if len(expense_List) == 0:
            print("No Expenses added. Enjoy Birthday party!")
        else:
            print("===== All Expenses =====")
            count = 1
            for eachexpense in expense_List:
                percentage = (eachexpense['amount'] / monthly_budget) * 100
                print(f"Expense no:{count} -> {eachexpense['date']}, {eachexpense['category']}, {eachexpense['amount']} ({percentage:.2f}%)")
                
                # High expense alert
                if percentage >= 50:
                    print("High expense alert!!!! This is more than 50% of your monthly pocket karch")
                
                count += 1  # Correctly indented

    # View Total Expenses
    elif choice == 3:
        total = sum(expense['amount'] for expense in expense_List)
        total_percentage = (total / monthly_budget) * 100
        print(f"\nTotal Expense: {total} ({total_percentage:.2f}% of monthly budget)")

    # View Total Expenses by Category
    elif choice == 4:
        if len(expense_List) == 0:
            print("No Expenses added. Enjoy Birthday party!")
        else:
            category_total = {}
            for expense in expense_List:
                if expense["category"] in category_total:
                    category_total[expense["category"]] += expense["amount"]
                else:
                    category_total[expense["category"]] = expense["amount"]

            print("\n===== Total Expenses by Category =====")
            for category, total in category_total.items():
                percentage = (total / monthly_budget) * 100
                print(f"{category} -> {total} ({percentage:.2f}% of monthly budget)")

    # View Expense by Date
    elif choice == 5:
        if len(expense_List) == 0:
            print("No expense added yet!")
        else:
            search_date = input("Enter date to see expense (DD/MM/YYYY): ")
            found = False
            print(f"\n==== Expenses on {search_date} ====")
            count = 1
            for expense in expense_List:
                if expense["date"] == search_date:
                    percentage = (expense['amount'] / monthly_budget) * 100
                    print(f"{count} -> {expense['category']}: {expense['amount']} ({percentage:.2f}%)")
                    count += 1
                    found = True
            if not found:
                print("No expenses found on this date.")

    # Exit
    elif choice == 6:
        print("Thank you for using my system!")
        break

    # Invalid Choice
    else:
        print("INVALID CHOICE. TRY AGAIN")