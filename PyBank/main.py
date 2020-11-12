'''* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period
'''
#Import Modules
import os
import csv 
#Path to collect data from the Resources folder
budget_data_csv = os.path.join("./Resources/budget_data_full.csv")
#Read in the CSV file
with open(budget_data_csv, 'r', encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
#Define the variables that will be used in the calculuations
    total_months = 0
    net_total = 0
    profit_losses_values = 0
    prev_rev = 0
    rev_change = 0
    rev_average = 0
    rev_change_list = []
    net_total_list = []
    greatest_increase = []
    greatest_decrease = []
    profit_losses = []
    profit_losses_list = []
    #Loop through the data
    for row in csvreader:
      #Calculate the total number of months included in the dataset 
      date = row[0]
      total_months += 1
      #Calculate the net total amount of "Profit/Losses" over the entire period
      profit_loss = int(row[1])
      net_total = net_total + profit_loss
      net_total_list.append(net_total)
      #Calculate the changes in "Profit/Losses" over the entire period
    for row in csvreader:
      profit_losses = int(row[1])
      #profit_losses_values = profit_losses_values + profit_losses
      #if profit_losses_values not in profit_losses_list:
      #  profit_losses_list.append(profit_losses_values)
      #rev_change = profit_losses - prev_rev
      #rev_change_list.append(rev_change)
      #prev_rev = profit_losses
      
      #Find the average of those changes
      #rev_average = sum(rev_change_list) / total_months

    #Calculate the greatest increase in profits (date and amount) over the entire period
    #greatest_increase = max()
    #Calculate the greatest decrease in losses (date and amount) over the entire period
    #greatest_decrease = min()
print("Financial Analysis")
print("----------------------------------------------------")      
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"{profit_losses}")
#print(rev_average)
#print(greatest_increase)
#print(greatest_decrease)


