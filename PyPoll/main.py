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

    # Complete list of candidates who received votes

    candidate_list = votes(candidate_data)

    candidate = []

    i = 0

    for i in candidate_list:
        
        candidate.append(str(i))

    print(candidate)

    # Percentage of votes each candidate won

    candidate_percentage = []

    i = 0

    for i in candidate_list:
        
        candidate_percentage.append(round((float(candidate_list[i]) / float(total_votes)) * 100, 3))

    print(candidate_percentage)

    # Total number of votes each candidate won

    candidate_votes = []

    i = 0

    for i in candidate_list:
        
        candidate_votes.append(round(int(candidate_list[i])))

    print(candidate_votes)

    # Winner of the election based on popular vote

    i = 0
    winner_votes = 0
    results = dict()

    for i in range (len(candidate_votes)):

        if candidate_votes[i] > winner_votes:

            winner_votes = candidate_votes[i]
            candidate_winner = str(candidate[i])
    
    results["name"] = candidate
    results["percentage"] = candidate_percentage
    results["votes"] = candidate_votes

    print(candidate_winner)

    print(results)

    # Print analysis results to Terminal

    # print("-----------------------------")
    # print("Election Results")
    # print("-----------------------------")
    # print(f"Total votes: {total_votes}")
    # print("-----------------------------")
    # print(f{})
    # print(f{})
    # print(f{})
    # print(f{})
    # print("-----------------------------")
    # print(f"Winner: {candidate_winner}")
    # print("-----------------------------")
    # # Save analysis results to txt file

    # analysis_path = os.path.join("Analysis", "analysis.txt")

    # text_file = open(analysis_path, "w+")
    # text_file.write("-----------------------------\n")
    # text_file.write("Financial analysis\n")
    # text_file.write("-----------------------------\n")
    # text_file.write(f"Total months: {total_months}\n")
    # text_file.write(f"Total profit: ${total_profit}\n")
    # text_file.write(f"Average change in profit: ${average_change}\n")
    # text_file.write(f"Greatest increase in profit: {increase_month} (${increase_profit})\n")
    # text_file.write(f"Greatest decrease in profit: {decrease_month} (${decrease_profit})\n")
    # text_file.write("-----------------------------\n")
    # text_file.close()

