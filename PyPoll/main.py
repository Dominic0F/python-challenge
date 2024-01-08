import csv
import os

# Create an "analysis" folder if it doesn't exist
if not os.path.exists("analysis"):
    os.mkdir("analysis")

# Initialize variables to store the analysis results
total_votes = 0
unique_candidates = []
candidate_votes = {}
winner = None
max_votes = 0

# Open and read the CSV file
with open('Resources/election_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    next(csv_reader)
    
    for row in csv_reader:
        # Extract data from the row
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        
        # Update total votes
        total_votes += 1
        
        # Update unique candidates list and their vote count
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# Determine the winner
for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        winner = candidate
        max_votes = votes

# Calculate and print the analysis results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Specify the path to save the results in the "analysis" folder
output_file_path = os.path.join("analysis", "election_results.txt")

# Create and write the results to a text file in the "analysis" folder
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    
    for candidate in unique_candidates:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
    
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Print a message indicating where the text file is saved
print(f"\nElection analysis results saved to '{output_file_path}'")
