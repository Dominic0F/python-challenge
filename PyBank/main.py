import csv
import os

# Create an "analysis" folder if it doesn't exist
if not os.path.exists("analysis"):
    os.mkdir("analysis")

# Initialize variables to store the analysis results
total_months = 0
total_profit = 0
previous_profit = None
average_change = 0
greatest_increase = ("", 0)
greatest_decrease = ("", 0)

# Open and read the CSV file
with open('Resources/budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    next(csv_reader)
    
    for row in csv_reader:
        # Extract data from the row
        month = row[0]
        profit = int(row[1])
        
        # Update total months and total profit
        total_months += 1
        total_profit += profit
        
        # Calculate average change
        if previous_profit is not None:
            change = profit - previous_profit
            average_change += change
        
        # Update greatest increase and greatest decrease
        if profit > greatest_increase[1]:
            greatest_increase = (month, profit)
        elif profit < greatest_decrease[1]:
            greatest_decrease = (month, profit)
        
        # Update previous profit for the next iteration
        previous_profit = profit

# Calculate the average change
average_change = round(average_change / (total_months - 1), 2)

# Print the analysis results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Specify the path to save the results in the "analysis" folder
output_file_path = os.path.join("analysis", "financial_analysis.txt")

# Save the results to a text file in the "analysis" folder
with open(output_file_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print a message indicating where the text file is saved
print(f"\nFinancial analysis results saved to '{output_file_path}'")
