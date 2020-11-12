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
import math
#Path to collect data from the Resources folder
election_data = os.path.join(".\Resources\election_data.csv")
#with open(election_data, encoding = "utf-8") as csvfile:
  #  csvreader = csv.reader(csvfile, delimiter = ",")
#The total number of votes cast in the dataset
with open(election_data, 'r', encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    total_votes = 0
    Kahn_votes = 0
    Correy_votes = 0
    Li_votes = 0
    O_Tooley_votes = 0
    candidates = []
    votes = []
    total_votes_list = []
    election_results = []
    Kahn_percentage = []
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        votes.append(candidate)
        if candidate not in candidates:
            candidates.append(candidate)
        
        total_votes += 1

    print("Election Results")
    print("--------------------------------------------------")
    print(total_votes)
    print("--------------------------------------------------")
    for candidate in candidates:
        count = 0
        for vote in votes:
            if candidate == vote:
                count = count + 1
        total_votes_list.append(count)
        print(candidate,count)



#complete list of candidates 
    
    for x in candidate:
        if x not in candidates:
            candidates.append(x)
            #election_results = candidates + str(count)
            #print(election_results)
    #print(candidates)
 
 #The percentage of votes each candidate won
    Kahn_percentage = (total_votes_list[0]/total_votes) * 100
    #Kahn_percentage_format = math.trunc(Kahn_percentage, 3)
    Correy_percentage = (total_votes_list[1]/total_votes) * 100
    Li_percentage = (total_votes_list[2]/total_votes) * 100
    O_Tooley_percentage = (total_votes_list[3]/total_votes) * 100
    #print(f"Kahn: {Kahn_percentage_format}% ({total_votes_list[0]})")
    #print(f"Correy: {Correy_percentage} ({Correy_votes})")
    #print(f"Li: {Li_percentage} ({Li_votes})")
    #print(f"O'Tooley: {O_Tooley_percentage} ({O_Tooley__votes})")
    #print("--------------------------------------------------")
#The winner of the election based on popular vote
#election_results ={
#   Kahn: "",
#   Correy: "",
#   Li: "",
#   O'Tolley: "",
# }
#election_winner = max(election_results, key=election_results.get)
print("-------------------------------------------------")
#print(f"Winner: {election_winner}")
        







