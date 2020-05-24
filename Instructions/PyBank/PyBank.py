#PyBank

import csv

csvpath = "Resources/budget_data.csv"

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Counter for months
    total_months = 0
    # Total profit
    total_profit = 0
    # Change List 
    total_changes = 0
    max_change = 0
    min_change = 0 
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        # The total number of months included in the dataset
        total_months = total_months + 1
        
        # The net total amount of "Profit/Losses" over the entire period
        total_profit = total_profit + int(row[1])
        
        # The average of the changes in "Profit/Losses" over the entire period
        
        if total_months == 1:
            last_profit = int(row[1])
        else:
            current_profit = int(row[1])
            change = current_profit - last_profit        
        # Add change to list
            total_changes = total_changes + change
            last_profit = current_profit 
        #The greatest increase in profits (date and amount) over the entire period
            if change > max_change:
                max_change = change
        
        #The greatest decrease in losses (date and amount) over the entire period
            if change < min_change:
                min_change = change
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months:{total_months}")
print(f"Total:${total_profit}")
print(f"Average Change:${total_changes / (total_months-1)}")
print(f"Greatest Increase in Profits:${max_change}")
print(f"Greatest Decrease in Profits:${min_change}")