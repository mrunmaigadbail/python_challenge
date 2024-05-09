# Modules

import csv

# Set path for input csv file
csvpath = "Resources/election_data.csv"

#set path for output text file
output_path = "analysis/results.txt"

#intilizing total votes to 0
total_votes = 0

#creating blank lists  
candidates =[]
votes=[]
vote_percents=[]


# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader) 
       
    # Read each row of data after the header
    for row in csvreader:  
        
        #counting total votes
        total_votes += 1
        
        #adding cadidates names to candidates list
        #checking column 3 of cvsfile and names to candidates list which are not already in list
        if row[2] not in candidates:
            candidates.append(row[2])
            # intializing votes list values to 0
            votes.append(0)     

        #calulating votes for each candidate
        i = candidates.index(row[2]) 
        votes[i]+=1  
    
    #calculating percent votes for each candidate
    for i in range(len(votes)):
        vote_percent=round(votes[i]/total_votes*100 ,3)
        vote_percents.append(vote_percent)
    
    #finding winner by checking maximum votes
    winner_votes=max(votes)
    winner_index=votes.index(winner_votes)
    winner=candidates[winner_index]
   
    #printing results
    print("Election Results")
    print("---------------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------------")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {vote_percents[i]}% ({votes[i]})")   
    print("---------------------------------")
    print(f"Winner: {winner}")
    print("---------------------------------")

# Open the text file using "write" mode. 
with open(output_path, 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------\n")
    text.write("Total Votes: "+ str(total_votes)+ "\n")
    text.write("---------------------------------\n")
    for i in range(len(candidates)):
        text.write(f"{candidates[i]}: "+ str(vote_percents[i])+"% ("+ str(votes[i])+")\n")   
    text.write("---------------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("---------------------------------\n")


