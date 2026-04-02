import matplotlib.pyplot as plt

def show_graph():
    category_total = {}

    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                category = row[2]
                amount = float(row[1])

                if category in category_total:
                    category_total[category] += amount
                else:
                    category_total[category] = amount

        categories = list(category_total.keys())
        amounts = list(category_total.values())

        plt.bar(categories, amounts)
        plt.title("Expense by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

    except:
        print("No data found!")