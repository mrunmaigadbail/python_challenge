# python_challenge

In this assignment we have give 2 different task
1. PyBank
    * We read into given csv file and write our results in text fileusing csv.reader and text.write
    * we successfully calculated
        1. The total number of months included in the dataset by adding each row in sheet after removing header
        2. The net total amount of "Profit/Losses" over the entire period by adding all the values in column 2 
        3. The changes in "Profit/Losses" over the entire period, by subtracting profit/loss with previous months profit/loss and then the average of those changes
        4. The greatest increase in profits amount over the entire period by using max function. then taking index of max value to find respective month
        5. The greatest decrease in profits amount over the entire period by using min function. then taking index of min value to find respective month
2. PyPoll
    * We read into given csv file and write our results in text file using csv.reader and text.write
    * we successfully calculated 
        1. The total number of votes cast by adding each row in sheet after removing header
        2. A complete list of candidates who received votes by creating candidates list and appending unique values in it.
        3. The total number of votes each candidate won by adding number of rows for each candidate and then adding it to list
        4. The percentage of votes each candidate won by dividing votes of each candidate by total votes multiplied by 100 then adding it to list
        5. The winner of the election based on popular vote by finding max value in votes to each candidate
* following is screen shots of working code
![pybank](https://github.com/mrunmaigadbail/python_challenge/assets/141286475/da8ad5a1-7e62-4cc6-8f0b-249509043cca)
![pypoll](https://github.com/mrunmaigadbail/python_challenge/assets/141286475/fb1623e9-2702-413a-8383-045f45b66b51)
