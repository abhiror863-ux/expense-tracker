import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Add Expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/etc): ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category, date])

    print("✅ Expense added!")

# View Expenses
def view_expense():
    total = 0
    category_total = {}

    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            print("\n--- Expenses ---")

            for row in reader:
                if len(row) < 4:
                    continue

                name, amount, category, date = row
                amount = float(amount)

                print(f"{date} | {name} | {category} | ₹{amount}")
                total += amount

                if category in category_total:
                    category_total[category] += amount
                else:
                    category_total[category] = amount

        print(f"\n💰 Total Expense: ₹{total}")

        print("\n📊 Category-wise:")
        for cat, amt in category_total.items():
            print(f"{cat}: ₹{amt}")

    except:
        print("No data found!")

# Monthly Report
def monthly_report():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            print(f"\n--- Report for {month} ---")

            for row in reader:
                if len(row) < 4:
                    continue

                if row[3].startswith(month):
                    print(f"{row[3]} | {row[0]} | {row[2]} | ₹{row[1]}")
                    total += float(row[1])

        print(f"\nTotal for {month}: ₹{total}")

    except:
        print("No data found!")

# Graph Function
def show_graph():
    category_total = {}

    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) < 4:
                    continue

                category = row[2]
                amount = float(row[1])

                if category in category_total:
                    category_total[category] += amount
                else:
                    category_total[category] = amount

        if not category_total:
            print("No data to show!")
            return

        categories = list(category_total.keys())
        amounts = list(category_total.values())

        plt.bar(categories, amounts)
        plt.title("Expense by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

    except Exception as e:
        print("Error:", e)

# Main Menu
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Report")
    print("4. Show Graph")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expense()
    elif choice == '3':
        monthly_report()
    elif choice == '4':
        show_graph()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
