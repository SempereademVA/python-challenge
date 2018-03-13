
# Student:  Marc Pitarys
# Date:  13 MAR 2018

#Import Modules
import os                        #Manipulates files and directories
import csv                       #Allows Python to parse CSV files
import datetime                  #Time Module


#Initialize the system

os.system("cls")                 #Clear the windows terminal screen
cwd =os.getcwd()                 #Get the current working directory

#Declare Variables
#These are temporary variables to speed up debugging
#file1 = 'election_data_1.csv'  #Input Data File Name
input_file = 'election_data_1.csv'  #Input Data File Name

#file1 = 'testdata.csv'


current_vote_total={}         #Current_vote_total is a dictionary with the candidates as the key and the vote counts as the value

super_vote_total={}           #The combined dictionary from multiple files

total_votes = 0  #Total of all the votes for all the candidates 

#############################################################################################
#
#                                   Define Functions
#
#############################################################################################


def calculate_poll_results(file1):
    
    #Vote_total is a dictionary with the candidate as the key and the vote count as the value
    #The file will be seached and when a new candidate is found, the dictionary will be appended
    #When a existing candidate is found in the file, the vote count for that candidate will be incremented
    vote_total={}

    print('Calculating results')
    #Initialize variables and the dictionary

    # Open the file in "read" mode ('r') and store the contents in the variable "f"
    with open(file1, 'r') as f:

        reader = csv.reader(f)      #Use Python's CSV routines
        next(reader)                #Skip the row with the column headings
        #row_data = next(reader)     #Note the row is in the format ID,County,Candidate
    #Process every row in the file by looking at the candidate name, searching for the name in the dictionary.
    #Then increment the vote count.  If the name is not in the directory create a new entry in the dictionary,
        for line in reader:
            if line[2] in vote_total:
                vote_total[line[2]]= vote_total[line[2]] + 1
            else:
                vote_total[line[2]] = 1
    return vote_total

def display_results(current_vote_total):

    total_votes = 0  #Total of all the votes for all the candidates

    for vote_count in current_vote_total.values():
        total_votes = total_votes + int(vote_count)

    print()
    print('Election Results')
    print('------------------------------------------')
    print('Total Votes ' + str(total_votes))
    print('------------------------------------------')
    for candidate, vote_count in current_vote_total.items():
    #Calculate the percentage of votes for the candidate.  This needs to be a floating point number
    #Then percent_vote is converted to a string with one decimal place and a % sign
        percent_out = '{percent_vote:.1%}'.format(percent_vote = float(current_vote_total[candidate])/float(total_votes))
        print(candidate + ': ' + percent_out + ' (' + str(vote_count) +')')

def write_results(current_vote_total, results_file):
    with open(results_file,'a') as f:

        total_votes = 0  #Total of all the votes for all the candidates

        for vote_count in current_vote_total.values():
            total_votes = total_votes + int(vote_count)
        f.write('\n')
        f.write('------------------------------------------\n')
        f.write('Total Votes ' + str(total_votes) + '\n')
        f.write('------------------------------------------\n')
        f.write('\n')

        for candidate, vote_count in current_vote_total.items():
        #Calculate the percentage of votes for the candidate.  This needs to be a floating point number
        #Then percent_vote is converted to a string with one decimal place and a % sign
            percent_out = '{percent_vote:.1%}'.format(percent_vote = float(current_vote_total[candidate])/float(total_votes))
            f.write(candidate + ': ' + percent_out + ' (' + str(vote_count) +')' +'\n')
        f.write('\n')

def find_winner(dictionary_of_results, results_file):
    with open(results_file, 'a') as f:
        highest_vote_count = 0
        for candidate, votes in dictionary_of_results.items():
            if int(votes) > int(highest_vote_count):
                highest_vote_count = votes
                highest_candidate = candidate
                tie = False
            elif int(votes) == int(highest_vote_count):
                tie == True
        if tie == False:
            print('------------------------------------------')
            print('Winner: ' + highest_candidate)
            print()
            f.write('-----------------------------------------\n')
            f.write('Winner: ' + highest_candidate +'\n')
            f.write('\n')
        else:
            print('------------------------------------------')
            print('We have a tie!  No winner')
            print()
            f.write('We have a tie!  No winner\n')
            f.write('\n')

         

    
            
         

########################################################################################################



##################################
#Main Program                    #
##################################

print()
print('Option 2 Now Processing')
print()

more_files = True
continue_counting = False

while more_files:        #Loop until there are no more files to process for the user.
    #The following are instructions printed to the terminal screen.
    print ('The current working directory is ---> ' + cwd)
    print()

    directory_for_output_file = cwd                      #Save this directory for writing the output file

    raw_data_file = input("Please provided the name of your raw data file. Don't forget the file extension -->  ")
    print('Please place the input file ' + raw_data_file + ' in a subdirectory called: Raw_Data')
    print()

    path1 = (cwd, 'Raw_Data', raw_data_file)
    file = '\\'.join(path1)
    print('Input File--> ' + file)
    print()
    try:
        checkfile = open(file, 'r')
        checkfile.close()
    except FileNotFoundError:
        print('File not found!')
        print()
        exit()

    #Get the Output File Name
    if continue_counting:
        output_data_file=input('Please provided the name of your output data file.  This file will contain previous computed results and the final results -->  ')
        print('Your output file ' + output_data_file + ' will be located here: ' + directory_for_output_file )
    else:
        output_data_file=input('Please provided the name of your output data file -->  ')
        print('Your output file ' + output_data_file + ' will be located here: ' + directory_for_output_file )
    print ()
        
    with open(output_data_file,'w') as f:
        f.write('\n')
        f.write('File Name: ' + raw_data_file + '\n')
        f.write('Data Processed on: ' + str(datetime.datetime.now()) + '\n')
        f.write('\n')
        
        f.write('Election Results\n')

    #This is where the the processing happens by calling functions
    if continue_counting:
        the_vote_total = calculate_poll_results(file)                #super_vote_total = {**the_vote_total, **previous_vote_total}
        super_vote_total = previous_vote_total
        for candidate_name in the_vote_total.keys():
            if candidate_name in previous_vote_total and candidate_name in the_vote_total:
                super_vote_total[candidate_name] = str(int(the_vote_total[candidate_name]) + int(previous_vote_total[candidate_name]))
            else:
                super_vote_total[candidate_name] = the_vote_total[candidate_name]
        display_results(super_vote_total)
        write_results(super_vote_total, output_data_file)
        find_winner(super_vote_total, output_data_file)
        the_vote_total = super_vote_total        #Need to update this variable so counting can continue beyond two files
    else:
        the_vote_total = calculate_poll_results(file)
        display_results(the_vote_total)
        write_results(the_vote_total, output_data_file)
        find_winner(the_vote_total, output_data_file)
    
    #Check to see if there are more files to process
    another_file = input('Do you have another file to process? (y/n) ')
    if another_file == 'y':
        add_more_to_file = input('Do you want to continue the count from the previous data file? (y/n) ')
        if add_more_to_file == 'y':
            previous_vote_total = the_vote_total
            continue_counting = True
        else:
            continue_counting = False
    if another_file != 'y':
        more_files = False

print()
print("Program Complete")
print()
