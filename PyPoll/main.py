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
election_data = os.path.join(".\Resources\election_data.csv")
with open(election_data, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
#The total number of votes cast in the dataset
with open(election_data, 'r', encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    total_votes = 0
    Kahn_votes = 0
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        total_votes += 1
    print(total_votes)

#complete list of candidates 
    candidates = []
    Kahn_percentage = []
    Kahn_votes = 0

    for x in candidate:
        if x not in candidates:
            candidates.append(x)
    #print(candidates)
    #Kahn_votes = []
    #Correy_votes = []
    #Li_votes = []
    #O_Tooley_votes = [] 
        if candidate == "Kahn": 
            Kahn_votes += 1
            Kahn_percentage = (Kahn_votes/total_votes) * 100
    print(f"Kahn: {Kahn_percentage}")
#if candidate == "Correy":
#        number_of_votes += 1
#print(f"{candidates[1]} + ": " + {Correy_percentage}")
 #   if candidate == "Li":
  #      number_of_votes += 1
#print(f"{candidates[2]} + ": " + {Li_percentage}")
 #   if candidate == "O'Tooley":
  #      number_of_votes += 1
#print(f"{candidates[3]} + ": " + {O_Tooley_Percentage}")





