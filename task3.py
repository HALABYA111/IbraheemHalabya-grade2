#"Daily Steps Tracker"

#Accepts the number of steps taken each day in the month as numbers separated by spaces.
input_steps = input("Enter the number of steps taken each day saparated by spaces:")

steps_string = input_steps.split()

steps = list(map(int, steps_string))
#Calculates the highest and lowest step counts.
highest_steps = max(steps)
lowest_steps = min(steps)
#Calculates the average daily step count.
avarage_steps = sum(steps) / len(steps)
#Sorts the step counts in descending order.
sorted_steps = sorted(steps, reverse=True)

avarage_steps_rounded = round (avarage_steps, 2)

print("\nSteps Analysis:")
print(f"Highest Steps: {highest_steps}")
print(f"Lowest Steps: {lowest_steps}")
print(f"Average Steps: {avarage_steps_rounded}")
print(f"Steps Sorted (Highest to Lowest): {sorted_steps}")

