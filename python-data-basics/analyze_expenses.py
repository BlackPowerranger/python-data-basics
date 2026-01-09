import csv

file_path = "data/expenses.csv"

total_spent = 0 
category_totals = {}
expense_count = 0

with open(file_path,newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        amount = float(row["amount"])
        category = row["category"]

        total_spent+=amount
        expense_count+=1

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category]+=amount

average_spent = total_spent/expense_count
highest_category = max(category_totals, key = category_totals.get)
highest_amount = category_totals[highest_category]

print("Total spent: ",total_spent)
print("\nSpending by category: ")
for category, amount in category_totals.items():
    print(f"{category}: {amount}")

print("\nAverage expense: ",average_spent)
print(f"Highest spending category: {highest_category} ({highest_amount})")
