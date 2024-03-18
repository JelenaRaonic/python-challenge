import csv
import os

#get the current working category 
current_directory = os.getcwd ()

#define the apsolute path of the file
file = os.path.join(current_directory, 'election_data.csv') 

#definy the path that is associated with file election_data.csv
file = '/Users/jelenaraonic/UTOR-VIRT-DATA-PT-02-2024-U-LOLC/python-challenge/PyPoll/Resources/election_data.csv'

all_rows = []
county = []
candidate = []


count_total_votes = 0

each_candidate = []
candidate_vote = []
total_votes = []
max_vote = 0
winner_candidate = []


#open the file in read mode 
with open(file, 'r') as csvfile:
    #created a csv.reader object
    csv_reader = csv.reader(csvfile, delimiter=",")  
    
    #skip the heather row 
    next(csv_reader)
    
#Do looping through the lists all_rows,candidate using append - adding more more elements to them
        
    for row in csv_reader:

    #count the number of ballot id which is same as number of our rows
        all_rows.append(row[0])
        total_votes = len(all_rows)

    #define candidate as a string and county as string 
        candidate.append(str(row[2]))
        county.append(str(row[1]))

        #calculate the count_total_votes
        count_total_votes = count_total_votes + 1
    
        each_candidate.append(str(row[2]))


#Print statement for Election results
print("-------------------------------------------")  
print("ELECTION RESULTS - PYPOLL")
print("-------------------------------------------")  
print ()
print(f"Total votes: {total_votes}") 
print ()
print("-------------------------------------------")  

for i in set(candidate):
    print(f"{i}, ({each_candidate.count(i)}), {round((each_candidate.count(i)/total_votes)*100)} % \n")
    max_vote = candidate.index(max(each_candidate))
    winner_candidate = each_candidate[int(max_vote)-1]


print("-------------------------------------------")
print(f'Winner:  {winner_candidate}')
print("-------------------------------------------")

#export Election results to text file
output_path = os.path.join('/Users/jelenaraonic/UTOR-VIRT-DATA-PT-02-2024-U-LOLC/python-challenge/PyPoll/analysis/analysis.txt')  
with open(output_path, 'w') as txt_file:
        

#Print statement for Election Results 

    txt_file.write(
    f"Election Results \n"
    f"---------------------------------\n")
    txt_file.write(
    f"Total votes: {total_votes}") 
    txt_file.write("\n")
    txt_file.write("---------------------------------\n")
    txt_file.write("\n")

    for i in set(candidate):
        txt_file.write(f"{i}, ({each_candidate.count(i)}), {round((each_candidate.count(i)/total_votes)*100)} % \n")
    max_vote = each_candidate.index(max(each_candidate))
    winner_election = each_candidate[int(max_vote)-1]


    txt_file.write("\n")
    txt_file.write("-----------------------------------\n")
    txt_file.write(f'Winner:  {winner_election} \n')
    txt_file.write("-----------------------------------\n")

    
    

    

   