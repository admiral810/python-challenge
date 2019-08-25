import os
import csv

# track number of months

months_count = []
profit_total = []

# Define the function and have it accept the budget data as its sole parameter
def budget(budget_data):

# Find the needed metrics
    month = str(budget_data[0])
    profit_loss = int(budget_data[1])

# Append lists
    months_count.append(month)
    profit_total.append(profit_loss)

# path to collect the CSV file
budget_csv = os.path.join("budget_data.csv")

# Read in the CSV file
with open(budget_csv, 'r') as budget_csv_file:  #'r' read the CSV 

    # Split the data on commas
    csv_reader = csv.reader(budget_csv_file, delimiter=',')
    header = next(budget_csv_file)

    ####print(f"CSV Header: {header}") - this was a test to print the headers that has been commented out####

    # Loop through the data
    for row in csv_reader:

        # run the budget function
        budget(row)

# calculate average, min, and max change

average_change = round(sum(profit_total)/len(months_count),2)

# define and calculate max and min change
max_change = round(max(profit_total),2)
min_change = round(min(profit_total),2)

# Find the index for the max and min values

max_index = (profit_total.index(max_change))
max_month_name = (months_count[max_index])

min_index = (profit_total.index(min_change))
min_month_name = (months_count[min_index])

# print statements
print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months_count)}")
print(f"Total: ${sum(profit_total)}")
print(f"Average Change: $ {average_change}")
print(f"Greatest Increase in Profits: {max_month_name} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month_name} (${min_change})")

# Set variable for output file
output_file = os.path.join("budget_summary.csv")

#  Open the output file 
with open(output_file, "w", newline="") as new_csv:
    writer = csv.writer(new_csv)

#  Write to output file
    writer.writerow(['Total Months', len(months_count)])
    writer.writerow(['Total', sum(profit_total)])
    writer.writerow(['Average Change', average_change])
    writer.writerow(['Greatest Increase in Profits (Month, Change)', max_month_name, max_change])
    writer.writerow(['Greatest Decrease in Profits (Month, Change)', min_month_name, min_change])
