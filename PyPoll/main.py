# PyPoll Homework by Matthias Zonneveld

# Modules
import os
import csv

# Function to count different candidates and their votes

def votes(data):

    d = dict()

    for c in data:
        if c not in d:
            d[c] = 1
        else:
            d[c] +=1
    return d

# Lists to store data
candidate_data = []

# Import the PyPoll election data
resources_path = os.path.join("Resources", "election_data.csv")

with open(resources_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read and save header

    csv_header = next(csvreader)

    # Store candidates in list

    for row in csvreader:

        candidate_data.append(row[2])

    # Total number of votes cast

    total_votes = len(candidate_data)

    # Create list for number of votes per candidate

    candidate_list = votes(candidate_data)

    # Create lists for candidates, percentage of votes per candidate and total number of votes per candidate
    
    candidate = []
    candidate_percentage = []
    candidate_votes = []

    for i in candidate_list:
        candidate.append(str(i))
        candidate_percentage.append(round((float(candidate_list[i]) / float(total_votes)) * 100, 1))
        candidate_votes.append(int(candidate_list[i]))

    # Winner of the election based on popular vote

    winner_votes = 0

    for i in range (len(candidate_votes)):

        if candidate_votes[i] > winner_votes:

            winner_votes = candidate_votes[i]
            candidate_winner = str(candidate[i])

    # Print analysis results to Terminal

    print("-----------------------------")
    print("Election Results")
    print("-----------------------------")
    print(f"Total votes: {total_votes}")
    print("-----------------------------")
    print(f"{candidate[0]}: {candidate_percentage[0]}% ({candidate_votes[0]})")
    print(f"{candidate[1]}: {candidate_percentage[1]}% ({candidate_votes[1]})")
    print(f"{candidate[2]}: {candidate_percentage[2]}% ({candidate_votes[2]})")
    print(f"{candidate[3]}: {candidate_percentage[3]}% ({candidate_votes[3]})")
    print("-----------------------------")
    print(f"Winner: {candidate_winner}")
    print("-----------------------------")

    # Save analysis results to txt file

    analysis_path = os.path.join("Analysis", "analysis.txt")

    text_file = open(analysis_path, "w+")
    text_file.write("-----------------------------\n")
    text_file.write("Election Results\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Total votes: {total_votes}\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"{candidate[0]}: {candidate_percentage[0]}% ({candidate_votes[0]})\n")
    text_file.write(f"{candidate[1]}: {candidate_percentage[1]}% ({candidate_votes[1]})\n")
    text_file.write(f"{candidate[2]}: {candidate_percentage[2]}% ({candidate_votes[2]})\n")
    text_file.write(f"{candidate[3]}: {candidate_percentage[3]}% ({candidate_votes[3]})\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Winner: {candidate_winner}\n")
    text_file.write("-----------------------------\n")
    text_file.close()

