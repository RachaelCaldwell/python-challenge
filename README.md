# python-challenge
The Module 3 Challenge is comprised of two Python tasks, PyBank and PyPoll.
* PyBank: Analysis of monthly financial data
* PyPoll: Analysis of election results


**Challenge 1:** PyBank

![image](https://github.com/RachaelCaldwell/python-challenge/assets/134207637/5416d2eb-29c6-41c2-99cb-a4a939219540)

The PyBank Python script analyzes a financial dataset called [budget_data.csv](https://github.com/RachaelCaldwell/python-challenge/blob/main/PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses".

The [PyBank Python script](https://github.com/RachaelCaldwell/python-challenge/blob/main/PyBank/PyBank.py) analyzes the records to calculate:
    
* The total number of months included in the dataset

* The net total amount of "Profit/Losses"

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits

* The greatest decrease in profits

[PyBank Financial Analysis](https://github.com/RachaelCaldwell/python-challenge/blob/main/PyBank/Analysis/PyBank.txt) 

    Financial Analysis
    ............................................................................
    Total Months: 86
    Net Total: ($22564198)
    Average Change: -8311.11
    Greatest Increase in Profits: Aug-16 ($1862002)
    Greatest Decrease in Profits: Feb-14 ($-1825558)


**Challenge 2:** PyPoll

![image](https://github.com/RachaelCaldwell/python-challenge/blob/main/Images/Vote_counting.png)

The PyPoll Python script analyzes a set of poll data called election_data.csv to help a small, rural town modernize its vote-counting process. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

The [PyPoll Python script](https://github.com/RachaelCaldwell/python-challenge/blob/main/PyPoll/PyPoll.py) analyzes the votes to calculate:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote

[PyPoll Election Analysis](https://github.com/RachaelCaldwell/python-challenge/blob/main/PyPoll/Analysis/PyPoll.txt)

    Election Results
    ............................................................................
    Total Votes:369711
    ............................................................................
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    ............................................................................
    Winner: Diana DeGette
