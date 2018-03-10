import os
os.system("clear")
#os.chdir

import csv


# Store the file path associated with the file (note the backslash may be OS specific) 

print('Option 1 Now Processing')
print()

#file = 'budget_data_1.csv'  #Input Data File Name
file = 'budget_data_2.csv'  #Input Data File Name

# Open the file in "read" mode ('r') and store the contents in the variable "text"
#You will see this displayed on the screen after the file is opened:
# <_io.TextIOWrapper name='input.txt' mode='r' encoding='cp1252'>

number_of_months = 0
total_revenue = 0
average_monthly_change_revenue = 0
monthly_change_revenue = 0
first_month_revenue = 0
second_month_revenue = 0
highest_change = 0
lowest_change = 0
total_changes = 0

with open(file, 'r') as reader:
    next(reader)                #Skip the row with the column names

    #Process the first line of data to initialize variables
    for k in range(1,3):
        print('Process the ' + str(k) +  ' line of data or ' + str(k+1)+  ' line in the file')
        second_line = reader.readline()
        print(second_line)
        number_of_months = number_of_months + 1
        Input_Date = second_line.strip('\n') 
        fields = Input_Date.split(',')
        print(fields)
        highest_date = fields[0]                    #Initialize Date with the highest average
        lowest_date = fields[0]
        print('Date: ' + highest_date)
        total_revenue = int(fields[1]) + total_revenue
        second_month_revenue = first_month_revenue
        first_month_revenue = int(fields[1])
        print('Revenue: $'+ str(total_revenue))
        print()
    monthly_change_revenue = first_month_revenue - second_month_revenue
    print('Monthly Change: ' + str(monthly_change_revenue))
    total_changes = total_changes + monthly_change_revenue
    print('Total Changes: ' + str(total_changes))
    second_month_revenue = first_month_revenue

 
   
    print('Process the rest of the file------------------')
    print()


    #Process the remaining rows in the file
    for line in reader:
        Input_Date = line.strip('\n')
        fields = Input_Date.split(',')
        print(fields)
        the_date = fields[0]
        print('Date: ' + the_date)
        the_revenue = fields[1]
        print('Revenue: $'+ the_revenue)
        #print('Length of Line: ' + str(len(line)))
        number_of_months = number_of_months + 1
        total_revenue = total_revenue + int(the_revenue)
        first_month_revenue = int(the_revenue)
        
        monthly_change_revenue = first_month_revenue - second_month_revenue
        print('Monthly Change: ' + str(monthly_change_revenue))
        total_changes = total_changes + monthly_change_revenue
        print('Total Changes: ' + str(total_changes))
        second_month_revenue = first_month_revenue
        if monthly_change_revenue >= highest_change:
            highest_change = monthly_change_revenue
            highest_date = the_date
            print('Highest Change found: ' + highest_date + ' ' + str(highest_change))
        if monthly_change_revenue <= lowest_change:
            lowest_change = monthly_change_revenue
            lowest_date = the_date
            print('Lowest Change found: ' + lowest_date + ' ' + str(lowest_change))

        print()
            

print('Total Changes: ' + str(total_changes))
average_monthly_change_revenue = total_changes/(number_of_months-1)
print()
print('Financial Analysis')
print('------------------------------------------')
print('Total Months: ' + str(number_of_months))
print('Total Revenue: $' + str(total_revenue))
print('Average Revenue: Change: $' + str(average_monthly_change_revenue))
print('Greatest Increase in Revenue: ' + highest_date + ' ' + '(' + str(highest_change) +')')
print('Greatest Decrease in Revenue: ' + lowest_date + ' ' + '(' + str(lowest_change) +')')
print()

#summary_file = "bank_results.txt"
summary_file = "bank_results2.txt"
with open(summary_file,'w') as f:
    f.write('Financial Analysis\n')
    f.write('------------------------------------------\n')
    f.write('Total Months: ' + str(number_of_months) + '\n')
    f.write('Total Revenue: $' + str(total_revenue)+ '\n')
    f.write('Average Revenue: Change: $' + str(average_monthly_change_revenue)+ '\n')
    f.write('Greatest Increase in Revenue: ' + highest_date + ' ' + '(' + str(highest_change) +')'+ '\n')
    f.write('Greatest Decrease in Revenue: ' + lowest_date + ' ' + '(' + str(lowest_change) +')'+ '\n')