#Import modules
import os
import csv

#Path to collect data from the Resources folder
election_data = os.path.join(".\Resources\election_data_full.csv")

#Read in the CSV file
with open(election_data, 'r', encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    total_votes = 0
    possible_winner = 0
    winner_votes = 0
    candidates = []
    votes = []
    candidate_votes = 0
    total_votes_list = []

#Loop through the data
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        votes.append(candidate)

#Calculate the total number of votes cast in the dataset
        total_votes += 1

#Create a complete list of candidates who received votes and the number of votes received
        if candidate not in candidates:
            candidates.append(candidate)
        
    for candidate in candidates:
        count = 0
        for vote in votes:
            if candidate == vote:
                count = count + 1
        total_votes_list.append(count)
        
#Calculate the percentage of votes each candidate won
    Kahn_percentage = round(((total_votes_list[0]/total_votes) * 100),2)
    Kahn_percentage_format = format((Kahn_percentage), '.3f')
    Correy_percentage = round(((total_votes_list[1]/total_votes) * 100),2)
    Correy_percentage_format = format((Correy_percentage), '.3f')
    Li_percentage = round(((total_votes_list[2]/total_votes) * 100),2)
    Li_percentage_format = format((Li_percentage), '.3f')
    O_Tooley_percentage = round(((total_votes_list[3]/total_votes) * 100),2)
    O_Tooley_percentage_format = format((O_Tooley_percentage), '.3f')

#Create a dictionary with election results 
election_results ={
    candidates[0]: total_votes_list[0],
    candidates[1]: total_votes_list[1],
    candidates[2]: total_votes_list[2],
    candidates[3]: total_votes_list[3],
 }

#Determine the winner of the election based on popular vote 
election_winner = max(election_results, key=election_results.get)

#Print Results
print("Election Results")
print("--------------------------------------------------")
print(F"Total Votes: {total_votes}")
print("--------------------------------------------------")
print(f"{candidates[0]}: {Kahn_percentage_format}% ({total_votes_list[0]})")
print(f"{candidates[1]}: {Correy_percentage_format}% ({total_votes_list[1]})")
print(f"{candidates[2]}: {Li_percentage_format}% ({total_votes_list[2]})")
print(f"{candidates[3]}: {O_Tooley_percentage_format}% ({total_votes_list[3]})")
print("--------------------------------------------------")
print(f"Winner: {election_winner}")
print("--------------------------------------------------")