#PyBank



import csv

csvpath = r"C:\Users\ckrokus\Desktop\Education\Homework\03-Python\Instructions\PyBank\Resources/budget_data.csv"

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
    profit_changes = []
    last_profit = 0
    current_profit = 0
    # Row Count
    row_count = 0
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        # The total number of months included in the dataset
        total_months = total_months + 1
        print(total_months)
        # The net total amount of "Profit/Losses" over the entire period
        total_profit = total_profit + int(row[1])
        print(total_profit)
        # The average of the changes in "Profit/Losses" over the entire period
        
        #If row_count == 0 then
        #last_profit = int(row[1])
        #else:
        current_profit = int(row[1])
        change = current_profit - last_profit        
        # Add change to list
        profit_changes.append(change)
        last_profit = current_profit 
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period