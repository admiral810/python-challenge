import os
import csv

# track lists
months_count = []
profit_total = []

# path to collect the CSV file
budget_csv = os.path.join("budget_data.csv")

# Read in the CSV file
with open(budget_csv, 'r') as budget_csv_file:  #'r' read the CSV 

    # Split the data on commas
    csv_reader = csv.reader(budget_csv_file, delimiter=',')
    header = next(budget_csv_file)

    # Loop through the data
    for row in csv_reader:
        
        # define variables
        month = str(row[0])
        profit_loss = int(row[1])

        # add to counts
        months_count.append(month)
        profit_total.append(profit_loss)
 
        # create list of month over month changes
        MoM_diff = [profit_total [i] - profit_total [i-1] for i in range(1,len(profit_total))]

# calculate average, min, and max change
average_diff = round(sum(MoM_diff)/(len(months_count)-1),2)
max_change = round(max(MoM_diff),2)
min_change = round(min(MoM_diff),2)

# Find the index for the max and min values
max_change_index = (MoM_diff.index(max_change))
max_month_change_name = (months_count[max_change_index + 1])

min_change_index = (MoM_diff.index(min_change))
min_month_change_name = (months_count[min_change_index + 1])


# print statements
print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months_count)}")
print(f"Total: ${sum(profit_total) : ,}")
print(f"Average Change: ${average_diff : ,}")
print(f"Greatest Increase in Profits: {max_month_change_name} (${max_change : ,})")
print(f"Greatest Decrease in Profits: {min_month_change_name} (${min_change : ,})")


# Set variable for output file
output_file = os.path.join("budget_summary.csv")

#  Open the output file 
with open(output_file, "w", newline="") as new_csv:
    writer = csv.writer(new_csv)

#  Write to output file
    writer.writerow(['Total Months', len(months_count)])
    writer.writerow(['Total', sum(profit_total)])
    writer.writerow(['Average Change', average_diff])
    writer.writerow(['Greatest Increase in Profits (Month, Change)', max_month_change_name, max_change])
    writer.writerow(['Greatest Decrease in Profits (Month, Change)', min_month_change_name, min_change])




