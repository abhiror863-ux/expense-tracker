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
    try:
        with open("data.csv", "r") as file:
            reader = list(csv.reader(file))
            print("\n--- Expenses ---")

            for i, row in enumerate(reader):
                if len(row) < 4:
                    continue
                print(f"{i+1}. {row[3]} | {row[0]} | {row[2]} | ₹{row[1]}")

    except:
        print("No data found!")

# Delete Expense
def delete_expense():
    try:
        with open("data.csv", "r") as file:
            data = list(csv.reader(file))

        view_expense()
        num = int(input("Enter expense number to delete: "))

        if 0 < num <= len(data):
            data.pop(num - 1)

            with open("data.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data)

            print("❌ Expense deleted!")
        else:
            print("Invalid number!")

    except:
        print("Error deleting expense!")

# Search by Category
def search_expense():
    category_search = input("Enter category to search: ").lower()

    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            print("\n--- Search Results ---")

            for row in reader:
                if len(row) < 4:
                    continue
                if row[2].lower() == category_search:
                    print(f"{row[3]} | {row[0]} | {row[2]} | ₹{row[1]}")

    except:
        print("No data found!")

# Graph
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

                category_total[category] = category_total.get(category, 0) + amount

        if not category_total:
            print("No data!")
            return

        plt.bar(category_total.keys(), category_total.values())
        plt.title("Expense by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

    except:
        print("Error generating graph!")

# Main Menu
while True:
    print("\n===== Expense Tracker PRO =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Search by Category")
    print("5. Show Graph")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expense()
    elif choice == '3':
        delete_expense()
    elif choice == '4':
        search_expense()
    elif choice == '5':
        show_graph()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
