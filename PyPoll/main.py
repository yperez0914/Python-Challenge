'''* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:'''

import os
import csv
#Path to collect data from the Resources folder
election_data = os.path.join(".\Resources\election_data_full.csv")
#with open(election_data, encoding = "utf-8") as csvfile:
  #  csvreader = csv.reader(csvfile, delimiter = ",")
#The total number of votes cast in the dataset
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
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        votes.append(candidate)
#A complete list of candidates who received votes
        if candidate not in candidates:
            candidates.append(candidate)
        
        total_votes += 1

    print("Election Results")
    print("--------------------------------------------------")
    print(F"Total Votes: {total_votes}")
    print("--------------------------------------------------")
    for candidate in candidates:
        count = 0
        for vote in votes:
            if candidate == vote:
                count = count + 1
        total_votes_list.append(count)
        
 #The percentage of votes each candidate won
    Kahn_percentage = round(((total_votes_list[0]/total_votes) * 100),2)
    Kahn_percentage_format = format((Kahn_percentage), '.3f')
    Correy_percentage = round(((total_votes_list[1]/total_votes) * 100),2)
    Correy_percentage_format = format((Correy_percentage), '.3f')
    Li_percentage = round(((total_votes_list[2]/total_votes) * 100),2)
    Li_percentage_format = format((Li_percentage), '.3f')
    O_Tooley_percentage = round(((total_votes_list[3]/total_votes) * 100),2)
    O_Tooley_percentage_format = format((O_Tooley_percentage), '.3f')
   
    print(f"{candidates[0]}: {Kahn_percentage_format}% ({total_votes_list[0]})")
    print(f"{candidates[1]}: {Correy_percentage_format}% ({total_votes_list[1]})")
    print(f"{candidates[2]}: {Li_percentage_format}% ({total_votes_list[2]})")
    print(f"{candidates[3]}: {O_Tooley_percentage}% ({total_votes_list[3]})")
    print("--------------------------------------------------")
#The winner of the election based on popular vote
    #for candidate_votes in total_votes_list:    
        #Kahn_votes = total_votes_list[0]
        #if Kahn_votes > possible_winner:
            #possible_winner = Kahn_votes
            #if Correy_votes > Kahn_votes:
               # possible_winner = Correy_votes
    #print(f"{Kahn_votes}")

election_results ={
    "Kahn": total_votes_list[0],
    "Correy": total_votes_list[1],
    "Li": total_votes_list[2],
    "O'Tolley": total_votes_list[3],
 }
election_winner = max(election_results, key=election_results.get)
print(f"Winner: {election_winner}")
print("--------------------------------------------------")
        







