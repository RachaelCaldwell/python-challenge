# Dependencies
import os
import csv

#Join Path
cwkdir = os.getcwd()
csvpath = os.path.join(cwkdir, 'Resources', 'budget_data.csv')

# Open and read csv
with open(csvpath, newline="") as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    csv_header = next(csvreader)

# Create list for months and profit_losses to store data
    months = []
    profit_losses = []
    
# Read each row of data after the header for total months and total profit_losses
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

# Calculate total months
    total_months = len(months)

# Calculate average_change
    change = []

    for x in range(1,len(profit_losses)):
        change.append(int(profit_losses[x] - int(profit_losses[x-1])))
        average_change = sum(change) / len(change)

# Calculate greatest increase and decrease in profits
        greatest_increase = max(change)
        greatest_decrease = min(change)
        max_month = months[change.index(max(change))]
        min_month = months[change.index(min(change))]

# Print to terminal
    print('Financial Analysis')
    print("............................................................................")
    print('Total Months: ' + str(total_months))    
    print('Net Total: ' + '($' + str(sum(profit_losses)) + ')')
    print('Average Change: ' + (str(round(average_change,2))))
    print('Greatest Increase in Profits: ' + str(months[change.index(max(change)) + 1]) + " " + '($' + str(greatest_increase) + ')')
    print('Greatest Decrease in Profits: ' + str(months[change.index(min(change)) + 1]) + " " + '($' + str(greatest_decrease) + ')')

# Output to a text file
file = open('PyBank.txt', 'w')
file.write('Financial Analysis' + "\n")
file.write("............................................................................" + "\n")
file.write('Total Months: ' + str(total_months) + "\n")    
file.write('Net Total: ' + '($' + str(sum(profit_losses)) + ')' + "\n")
file.write('Average Change: ' + (str(round(average_change,2))) + "\n")
file.write('Greatest Increase in Profits: ' + str(months[change.index(max(change)) + 1]) + " " + '($' + str(greatest_increase) + ')'+ "\n")
file.write('Greatest Decrease in Profits: ' + str(months[change.index(min(change)) + 1]) + " " + '($' + str(greatest_decrease) + ')'+ "\n")