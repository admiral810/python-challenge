import os
import csv

# track number of votes

vote_count = []


# Define the function for count of votes, one sole parameter
def election(election_data):

# Find the number of total voles
    vote = str(election_data[0])
    candidate = str(election_data[2])

# Append vote count list
    vote_count.append(vote)





# path to collect the CSV file
poll_csv = os.path.join("election_data.csv")

# Read in the CSV file
with open(poll_csv, 'r') as poll_csv_file:  #'r' read the CSV 

    # Split the data on commas
    csv_reader = csv.reader(poll_csv_file, delimiter=',')
    header = next(poll_csv_file)

    ##print(f"CSV Header: {header}") - initial test to make sure file is pulling in##

    candidate_of_interest = "Kahn"

    # Loop through the data
    for row in csv_reader:

        # run the budget function
        if candidate_of_interest == row[2]:
            election(row)

# calculate the total votes
print(f"total votes are:  {len(vote_count)}")


#!!!figure out how to dedupe candidates!!!  candidate_list_dupes = []  #contains duplicate candidates
#!!!figure out how to dedupe candidates!!!  candidate_list = list(set(candidate_list_dupes))  #removed duplicate candidates
#!!!figure out how to dedupe candidates!!! print(f"candidates are:  {candidate_list}")
#!!!figure out how to dedupe candidates!!!      candidate_list_dupes.append(candidate)