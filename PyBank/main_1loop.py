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
    prev_rev = 0
    rev_change = 0
    rev_average = 0
    rev_change_total = 0
    greatest_increase = 0
    greatest_decrease = 0
    firstrow = next(csvreader)
    total_months += 1
    net_total += int(firstrow[1])
    prev_rev += int(firstrow[1])
    #Loop through the data
    for row in csvreader:
      #Calculate the total number of months included in the dataset 
      date = row[0]
      total_months += 1

      #Calculate the net total amount of "Profit/Losses" over the entire period
      profit_loss = int(row[1])
      net_total = net_total + profit_loss
      
      #Calculate the changes in "Profit/Losses" over the entire period
      rev_change = profit_loss - prev_rev
      prev_rev = profit_loss

      #Find the average of those changes
      rev_change_total += rev_change
      rev_average = round((rev_change_total/ total_months),2)
    
      #Calculate the greatest increase & in profits (date and amount) over the entire period
      if rev_change >= greatest_increase:
        greatest_increase = rev_change

      #Calculate the greatest decrease in losses (date and amount) over the entire period
      if rev_change < greatest_decrease:
        greatest_decrease = date
        greatest_decrease = rev_change
                
print("Financial Analysis")
print("----------------------------------------------------")      
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: {rev_average}")
print(f"Greatest Increase in Profits: {date} $({greatest_increase})")
print(f"Greatest Decrease in Profits: {date} $({greatest_decrease})")
print("-----------------------------------------------------")



