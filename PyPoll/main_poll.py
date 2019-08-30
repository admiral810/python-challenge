import os
import csv
import statistics 

# Create lists to store each candidate occurance in dataset
candidate_with_dupes = []

# path to collect the CSV file
poll_csv = os.path.join("election_data.csv")

# Read in the CSV file
with open(poll_csv, 'r') as poll_csv_file:  #'r' read the CSV 

    # Split the data on commas
    csv_reader = csv.reader(poll_csv_file, delimiter=',')
    header = next(poll_csv_file)

    # Loop through the data to create a list of all candidates - note it has duplicate values
    for row in csv_reader:

        candidate_with_dupes.append(row[2])
        total_votes = len(candidate_with_dupes)

    # De-dupe the candidate list
    candidate_list = list(set(candidate_with_dupes))


    # Length of candidates to calculate the total number of candidates for ranges
    cand_one_votes = candidate_with_dupes.count (candidate_list[0])
    cand_one_percent = round(cand_one_votes / total_votes * 100 , 2)
    
    cand_two_votes = candidate_with_dupes.count (candidate_list[1])
    cand_two_percent = round(cand_two_votes / total_votes * 100 , 2)
    
    cand_three_votes = candidate_with_dupes.count (candidate_list[2])
    cand_three_percent = round(cand_three_votes / total_votes * 100 , 2)
    
    cand_four_votes = candidate_with_dupes.count (candidate_list[3])
    cand_four_percent = round(cand_four_votes / total_votes * 100 , 2)

    # Determine winner by finding the mode of the candidate list
    winner = statistics.mode(candidate_with_dupes)


# print statements of results

print(f"-----------------------")
print(f"Total Votes: {total_votes : ,}")
print(f"-----------------------")
print(f" {candidate_list[0]}: {cand_one_percent}% ({cand_one_votes : ,} )")
print(f" {candidate_list[1]}: {cand_two_percent}% ({cand_two_votes : ,} )")
print(f" {candidate_list[2]}: {cand_three_percent}% ({cand_three_votes : ,} )")
print(f" {candidate_list[3]}: {cand_four_percent}% ({cand_four_votes : ,} )")
print(f"-----------------------")
print(f"Winner:  {winner}")

# Set variable for output file
output_file = os.path.join("poll_summary.csv")

#  Open the output file 
with open(output_file, "w", newline="") as new_csv:
    writer = csv.writer(new_csv)

#  Write to output file
    writer.writerow(['Candidate', 'Vote Count', 'Percent'])
    writer.writerow(['Total Votes', total_votes, '100'])
    writer.writerow([candidate_list[0], cand_one_votes, cand_one_percent])
    writer.writerow([candidate_list[1], cand_two_votes, cand_two_percent])
    writer.writerow([candidate_list[2], cand_three_votes, cand_three_percent])
    writer.writerow([candidate_list[3], cand_four_votes, cand_four_percent])
    writer.writerow(['--', '--', '--'])
    writer.writerow(['Overall winner: ', winner])