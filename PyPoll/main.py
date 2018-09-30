import os
import csv

csvpath = os.path.join("election_data.csv")

total_votes_cast=0
candidate_list = {}
winner=""
winner_votes=0

with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	next(csvreader, None)

	for row in csvreader:
		voter_id = row[0]
		county = str(row[1])
		candidate = str(row[2])
		total_votes_cast = total_votes_cast + 1
		if candidate in candidate_list:
			candidate_list[candidate] = candidate_list[candidate] + 1
		else:
			candidate_list[candidate] = 1
			

print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes_cast}')
for key, value in candidate_list.items():
	if (value > winner_votes):
		winner_votes = value
		winner = key
	percent = '{percent:.3%}'.format(percent=value/total_votes_cast)
	print(f'{key}: {percent} ({value})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")
