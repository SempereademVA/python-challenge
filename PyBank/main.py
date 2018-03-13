#Name:  Marc Pitarys
#Date:  13 MAR 18


#Import Modules
import os                        #Manipulates files and directories
import csv                       #Allows Python to parse CSV files
import datetime                  #Time Module
#import itertools



#Initialize the system

os.system("cls")                 #Clear the windows terminal screen
cwd =os.getcwd()                 #Get the current working directory



#Declare Variables

number_of_months = 0
total_revenue = 0
average_monthly_change_revenue = 0
monthly_change_revenue = 0
first_month_revenue = 0
second_month_revenue = 0
highest_change = 0
lowest_change = 0
total_changes = 0

#Introductory Text
print('               Welcome to the Pybank Program')
print('This program reads a csv file provided by the user and performs a financial analysis.')
print('The input file contains two columns of data: Date(Month/Year) and Revenue')
print('An analysis is performed on the data.  The program generates the following results:')
print('1. Total Number of Months Analyzed')
print('2. Total Revenue')
print('3. Average Revenue Change')
print('4. Greatest Increase in Revenue and the month it occurred')
print('5. Greatest Decrease in Revenue: ')
print()
print('The output of the program is stored in a text file located in the working directory.  File Name: Analysis_output.txt')
print()

#Get the Input File Name
cwd =os.getcwd()
print ('The current working directory is ---> ' + cwd)
print()
directory_for_output_file = cwd                      #Save this directory for writing the output file
raw_data_file=input("Please provided the name of your raw data file. Don't forget the file extension -->  ")
print()
print('Please place the input file ' + raw_data_file + ' in a subdirectory called: Raw_Data')
path1 = (cwd, 'Raw_Data', raw_data_file)
file= '\\'.join(path1)
print('Input File--> ' + file)
print()

#Get the Output File Name
output_data_file=input('Please provided the name of your output data file -->  ')
print('Your output file ' + output_data_file + ' will be located here: ' + directory_for_output_file )
print ()

# Open the file in "read" mode ('r') and store the contents in the variable "f"
with open(file, 'r') as f:

    reader = csv.reader(f)      #Use Python's CSV routines
    next(reader)                #Skip the row with the column headings
    second_line = next(reader)   #Reading the first row of data in file for computing change in revenue
    first_line = next(reader)  #Now read the row with the first available data in the file
    number_of_months = 2         #Just processed the first two months in the file
    #Initialize dates with highest and lowest changes in revenue with the first available month used in computing revenue
    highest_date = first_line[0]
    lowest_date = first_line[0]
    #Compute the total revenue for the first two months
    total_revenue = int(second_line[1]) + int(first_line[1])
    #Compute the monthly change in revenue for the first two available months
    second_month_revenue = int(second_line[1])
    first_month_revenue = int(first_line[1])
    monthly_change_revenue = first_month_revenue - second_month_revenue
    print('The first monthly change is: ' + str(monthly_change_revenue))
    #Keep a total of the monthly changes in revenues for the final average computation
    total_changes = total_changes + monthly_change_revenue
    #Update the previous months revenue with the current month for calculating monthly change in revenues
    second_month_revenue = first_month_revenue 
  
    #print('Process the rest of the file------------------')
    #print()

    #Process the remaining rows in the file
    for line in reader:
        Input_Date = line[0]
        #print('Date: ' + Input_Date)
        the_revenue = line[1]
        #print('Revenue: $'+ the_revenue)
        number_of_months = number_of_months + 1
        total_revenue = total_revenue + int(the_revenue)
        first_month_revenue = int(the_revenue)
        
        monthly_change_revenue = first_month_revenue - second_month_revenue
        #print('Monthly Change: ' + str(monthly_change_revenue))
        total_changes = total_changes + monthly_change_revenue
        #print('Total Changes: ' + str(total_changes))
        second_month_revenue = first_month_revenue
        if monthly_change_revenue >= highest_change:
            highest_change = monthly_change_revenue
            highest_date = Input_Date
            #print('Highest Change found: ' + highest_date + ' ' + str(highest_change))
        if monthly_change_revenue <= lowest_change:
            lowest_change = monthly_change_revenue
            lowest_date = Input_Date
            #print('Lowest Change found: ' + lowest_date + ' ' + str(lowest_change))

        #print()
            

#Compute the Average Monthly Change in Revenue
average_monthly_change_revenue = total_changes/(number_of_months-1)

#Print the Summary of the Analysis

print()
print('Financial Analysis')
print('------------------------------------------')
print('Total Months: ' + str(number_of_months))
print('Total Revenue: $' + str(total_revenue))
print('Average Revenue: Change: $' + str(round(average_monthly_change_revenue)))
print('Greatest Increase in Revenue: ' + highest_date + ' ' + '(' + str(highest_change) +')')
print('Greatest Decrease in Revenue: ' + lowest_date + ' ' + '(' + str(lowest_change) +')')
print()

#Store the results in the output file

with open(output_data_file,'w') as f:
    f.write('Financial Analysis\n')
    f.write('Data Processed on: ' + str(datetime.datetime.now())+'\n')
    f.write('------------------------------------------\n')
    f.write('Total Months: ' + str(number_of_months) + '\n')
    f.write('Total Revenue: $' + str(total_revenue)+ '\n')
    f.write('Average Revenue: Change: $' + str(round(average_monthly_change_revenue))+ '\n')
    f.write('Greatest Increase in Revenue: ' + highest_date + ' ' + '(' + str(highest_change) +')'+ '\n')
    f.write('Greatest Decrease in Revenue: ' + lowest_date + ' ' + '(' + str(lowest_change) +')'+ '\n')
    f.write('\n')

print()
print('*************************Processing Complete!*************************')
print()