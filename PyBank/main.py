import csv
import os

#get the current working category 
current_directory = os.getcwd ()

#define the apsolute path of the file
file = os.path.join(current_directory, 'python-challenge/PyBank/Resources/budget_data.csv') 

#definy the path that is associated with file budget_data.csv
file = '/Users/jelenaraonic/UTOR-VIRT-DATA-PT-02-2024-U-LOLC/python-challenge/PyBank/Resources/budget_data.csv'

all_rows = []
profit_loss = []

total_profit_loss = 0
i = 1



#open the file in read mode 
with open(file, 'r') as csvfile:
    #created a csv.reader object
    csv_reader = csv.reader(csvfile, delimiter=",")  
    
    #skip the heather row 
    next(csv_reader)

    #Do looping through the lists all rows and profit_loss using append - adding more more elements to them
    
    for row in csv_reader:

    #calculate the total_profit_loss of the entire period
        total_profit_loss = total_profit_loss + int(row[1])
        profit_loss.append(int(row[1]))

    #count the number of months which is same as number of all_ rows
        all_rows.append(row[0])
        total_months = len(all_rows)

    #calculate the changes of profit_loss taking next profit_loss and suptructing previous one 
    changes = [profit_loss[i+1] - profit_loss[i] for i in range(len(profit_loss)-1)]

    #Calculate average change as a sum devided by number of rows less then 1
    average_change = sum(changes) / (len(all_rows)-1)

    #round avarage_change 
    average_change = round (average_change,2)
    
    #Greatest _increase and greatest_decrease we can get through pulling max and min values of changes of profit_loss we calculated previously
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

    #We need to conncet greatest_increase change and greatest_decrease change with corresponding date when it occured  

date_index_greatest_increase = all_rows[changes.index(greatest_increase)]
date_index_greatest_decrease = all_rows[changes.index(greatest_decrease)]



#Print statement for all findings in our Financial Analysis PyBank 
print ()
print("Financial Analysis PyBank")
print("---------------------------------------")  
print ()
print(f"Total number of months: {total_months}") 
print ()
print(f"Total profit/loss: ${total_profit_loss}")
print ()
print(f"Average Change: ${average_change}")
print()
print(f"Gratest Increase in Profits: {date_index_greatest_increase} (${greatest_increase:})")
print()
print(f"Greatest Decrease in Profits: {date_index_greatest_decrease} (${greatest_decrease:})")
print()
    


#export results of Financial Analysis to text file
output_path = os.path.join('/Users/jelenaraonic/UTOR-VIRT-DATA-PT-02-2024-U-LOLC/python-challenge/PyBank/analysis/analysisresult.txt')  
with open(output_path, 'w') as txt_file:
        

#Print statement for all findings in our Financial Analysis PyBank 

    txt_file.write(
    f"FINANCIAL ANALYSIS PYBANK \n"
    f"-------------------------------\n")
    txt_file.write("\n")
    txt_file.write(f"Total number of months: {total_months}\n") 
    txt_file.write("\n")
    txt_file.write(f"Total profit/loss: ${total_profit_loss}\n")
    txt_file.write("\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits: {date_index_greatest_increase} (${greatest_increase:})\n")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits: {date_index_greatest_decrease} (${greatest_decrease:})")

    

