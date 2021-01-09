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

# Lists and variables
candidate_data = []
candidate = []
candidate_percentage = []
candidate_votes = []
total_votrs = 0
winner_votes = 0
winner = ""

# Import the PyPoll election data
resources_path = os.path.join("Resources", "election_data.csv")

with open(resources_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read and save header

    csv_header = next(csvreader)

    # Store candidates in list

    for row in csvreader:
        candidate_data.append(row[2])

    # Total number of votes cast

    total_votes = len(candidate_data)

    # Create dictionary for number of votes per candidate

    candidate_dict = votes(candidate_data)

    # Create lists for candidates, percentage of votes per candidate and total number of votes per candidate

    for i in candidate_dict:
        candidate.append(str(i))
        candidate_percentage.append(round((float(candidate_dict[i]) / float(total_votes)) * 100, 1))
        candidate_votes.append(int(candidate_dict[i]))

    # Winner of the election based on popular vote

    for i in range (len(candidate_dict)):
        if candidate_votes[i] > winner_votes:
            winner_votes = candidate_votes[i]
            winner = str(candidate[i])

    # Print analysis results to Terminal

    print("-----------------------------")
    print("Election Results")
    print("-----------------------------")
    print(f"Total votes: {total_votes}")
    print("-----------------------------")
    for i in range (len(candidate_dict)):
        print(f"{candidate[i]}: {candidate_percentage[i]}% ({candidate_votes[i]})")
    print("-----------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------")

    # Save analysis results to txt file

    analysis_path = os.path.join("Analysis", "analysis.txt")

    text_file = open(analysis_path, "w+")
    text_file.write("-----------------------------\n")
    text_file.write("Election Results\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Total votes: {total_votes}\n")
    text_file.write("-----------------------------\n")
    for i in range (len(candidate_dict)):
        text_file.write(f"{candidate[i]}: {candidate_percentage[i]}% ({candidate_votes[i]})\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-----------------------------\n")
    text_file.close()

