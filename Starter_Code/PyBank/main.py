import csv

# Set path for input csv file 
csvpath = "Resources/budget_data.csv"

# set path for output text file
output_path = "analysis/results.txt"

# intilizing variables and lists
count_months = 0
total= 0
last_month_value = 0
changes = []
month_changes =[]

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
       
    # Read each row of data after the header
    for row in csvreader:
        #counting number of month by adding each row after header    
        count_months += 1
        
        #calculating total by converting to integer and adding values from column 2  
        total+= int(row[1])

        #calulating change and adding values to changes list and respective month to month_changes list
        if(count_months==1):
            last_month_value = int(row[1])

        else:
            change = int(row[1]) - last_month_value
            changes.append(change)
            last_month_value = int(row[1])
            month_changes.append(row[0])
    
    #finding average channge
    change_avg= round(sum(changes)/len(changes),2)
    
    #finding greatest increase profits
    greatest_increase=max(changes)
    greatest_increase_index=changes.index(greatest_increase)
    greatest_inc_month= month_changes[greatest_increase_index]

    #finding greatest decrease in profits    
    greatest_decrease=min(changes)
    greatest_decrease_index=changes.index(greatest_decrease)
    greatest_dec_month= month_changes[greatest_decrease_index]
    
    #printing Results
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${change_avg}")
    print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_decrease})")

# Open the file using "write" mode and writing results. 
with open(output_path, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("---------------------------------\n")
    text.write("Total Months: "+ str(count_months)+ "\n")
    text.write("Total: $" + str(total) +"\n")
    text.write("Average Change: $" +str(change_avg)+"\n")
    text.write("Greatest Increase in Profits: "+str(greatest_inc_month) +" ($" + str(greatest_increase)+")\n")
    text.write("Greatest Decrease in Profits: "+str(greatest_dec_month) +" ($" + str(greatest_decrease)+")\n")

