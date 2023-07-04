# Dependencies
import os
import csv

# Join path
cwkdir = os.getcwd()
csvpath = os.path.join(cwkdir, 'Resources', 'election_data.csv')

# Set variables
total_votes = 0
candidate_list = []
candidate_votes = {}
candidate_results = ""
winner = ""
win_count = 0
win_percent = 0

# Open and read csv
with open(csvpath, newline="") as election_data:
    csvreader = csv.reader(election_data, delimiter=',')
    csv_header = next(csvreader)

# Calculate total votes and votes per candidate
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Calculate voter percentage per candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results += f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
    
# Calculate winner based on popular vote
        if candidate_votes[candidate_name] > win_count:
            winner = candidate_name
            win_count = candidate_votes[candidate_name]

#Print to terminal
print('Election Results')
print("............................................................................")
print('Total Votes:'+ str(total_votes))
print("............................................................................")
print(candidate_results)
print("............................................................................")
print(f"Winner: " + winner)

# Output to text file
file = open('PyPoll.txt', 'w')
file.write('Election Results' + "\n")
file.write("............................................................................" + "\n")
file.write('Total Votes:'+ str(total_votes) + "\n")   
file.write("............................................................................" + "\n") 
file.write(candidate_results)
file.write("............................................................................" + "\n") 
file.write(f"Winner: " + winner+ "\n")