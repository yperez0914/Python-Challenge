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
budget_data_csv = os.path.join("./Resources/budget_data.csv")
with open(budget_data_csv, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    num_months = 0
    for row in csvreader:
        date = row[0]
        Profits_Losses = row[1]
      
        for date in csvreader:
            num_months += 1
            print(num_months)


#(Print CSV reader to check formatting)
  #  print(csvreader)
  #  csv_header = next(csvreader)
  #  print(f'CSV Header: {csv_header}')
    
    #for months in csvreader:
      #  num_months += 1
      #  print(num_months)

#Define the function and have it accept the 'budget_data' as its sole parameter
#def budget_calculations (budget_data):
#define variables that will be used in the formulas

#Calculate the total number of months included in the dataset 