print("Welcome to Tip Calculator!\n")

bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = (bill / people) * (1 + (percent/100))
print(f"Each person should pay: ${tip:.2f}") 