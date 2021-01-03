# PyBank Homework by Matthias Zonneveld

# Modules
import os
import csv

# Lists to store data
month = []
profit = []

# Import the PyBank budget data
resources_path = os.path.join("Resources", "budget_data.csv")

with open(resources_path, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header

    next(csvreader)

    # Store month and profit info in lists

    for row in csvreader:
        
        month.append(row[0])

        profit.append(int(row[1]))

    # Total number of months included in dataset    

    total_months = len(month)

    # Net total amount of Profit/Losses

    total_profit = sum(profit)
    
    # Average of changes in Profit/Losses

    i = 0
    average = []

    for i in range (len(profit)):
        for j in range(i + 1, len(profit)):
            difference = profit[j] - profit[i]
            average.append(difference)

    average_change = int(sum(average) / len(average))

    # Greatest increase in profits
    
    i = 0
    increase_profit = 0

    for i in range (len(profit)):
        difference = 0
        for j in range(i + 1, len(profit)):
            difference = profit[j] - profit[i]
            if 0 <= increase_profit < difference:
                increase_profit = difference
                increase_month = str(month[j])

    # Greatest decrease in profits

    i = 0
    decrease_profit = 0

    for i in range (len(profit)):
        difference = 0
        for j in range(i + 1, len(profit)):
            difference = profit[j] - profit[i]
            if 0 >= decrease_profit > difference:
                decrease_profit = difference
                decrease_month = str(month[j])

    # Print analysis results to Terminal

    print("Financial analysis")
    print("-----------------------------")
    print(f"Total months: {total_months}")
    print(f"Total profit: $ {total_profit}")
    print(f"Average change: $ {average_change}")
    print(f"Greatest increase in profits: {increase_month} ($ {increase_profit})")
    print(f"Greatest decrease in profits: {decrease_month} (${decrease_profit})")

    # Save analysis results to txt file

    analysis_path = os.path.join("Analysis", "analysis.txt")

    text_file = open(analysis_path, "w+")
    text_file.write("Financial analysis\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Total months: {total_months}\n")
    text_file.write(f"Total profit: $ {total_profit}\n")
    text_file.write(f"Greatest increase in profits: {increase_month} ($ {increase_profit})\n")
    text_file.write(f"Greatest decrease in profits: {decrease_month} (${decrease_profit})\n")
    text_file.close()

