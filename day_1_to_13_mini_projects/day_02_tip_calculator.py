# Calculates how much each person should pay based on inputs of total bill, tip percentage, and number of people

print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? $"))
tip = int(input("How much percentage of tip would you like to give? 10, 12, or 15? %"))
people = int(input("How many people to split the bill? "))
total_bill = bill * (1 + tip/100)

print(f"Each person should pay: ${round(total_bill / people, 2)}")
