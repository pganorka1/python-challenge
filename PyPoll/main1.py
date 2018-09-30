
#You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
# The winner of the election based on popular vote.


#As an example, your analysis should look similar to the one below:


#Election Results
 
# -------------------------
 # Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
  
 
import os
import csv
file_path = os.path.join("election_data1.csv")

total_vote_cast = []
candidates = []
percent_vote = []
candidate_vote = []
Winner = []

total_vote_cast= 0
candidate = 0
percent_vote= 0
candidate_vote = 0
with open(file_path,newline ="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter= ",")
   csv_header = next(csvreader)
  
   total_vote_cast = []
   total_votes_cast= [row for row in csvreader]
   # create a list to be used in the function/s
   print(total_vote_cast)
  
   # function for number of voters
def voter_counter(total_vote_cast):
   num = 0
   for each in total_vote_cast:
       num = num + 1
   return num

# function to find unique candidates
def unique_candidates (total_vote_cast):
   tally = [i[2] for i in total_vote_cast] # list of candidates
   unique = {}
   for i in tally:
       if not i in unique:
           unique[i] = 1
       else:
           unique[i] += 1
   return unique

# calculate percent votes per candidate
def pct_votes(total_vote__cast):
   values = unique_candidates(total_vote_cast).values()
   pct = [((float(i) / voter_counter(total_vote_cast)) * 100) for i in values]
   return pct

###
# 
   print("----------------------------------------------------------")
   print("total_vote_cast")
   print("----------------------------------------------------------")
   print("candidate: " + str(countpercent))
   print("candidate: " + str(countpercent))
   print("candidate: " + str(countpercent))
   print("----------------------------------------------------------")

#with open("financial_analysis.txt", "w") as text:
   #text.write("----------------------------------------------------------\n")
   #text.write("  Financial Analysis"+ "\n")
   #text.write("----------------------------------------------------------\n\n")
   #text.write("    total_vote_count: " + str(count) + "\n")
   #text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
   #text.write("    Average Change: " + "$" + str(int(average_change_profits)) + "\n")
   #text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
   #text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
   #text.write("----------------------------------------------------------\n")
