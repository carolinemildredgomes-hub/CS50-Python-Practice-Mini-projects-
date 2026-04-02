import statistics

# Take input from user
marks_input = input("Enter student marks separated by space: ")

# Convert input into a list of integers
marks = [int(x) for x in marks_input.split()]

# Calculate statistics
average_marks = statistics.mean(marks)
highest_marks = max(marks)
lowest_marks = min(marks)

# Print results
print("\nStudent Marks Statistics:")
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
