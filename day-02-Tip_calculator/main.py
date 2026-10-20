print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill ?: $"))
tip_prcnt = int(input("How much tip would you like to give? 10, 12 or 15?: "))
tip_amount = float(int(tip_prcnt) / 100)
people = int(input("How many people to split the bill?: "))
bill_per_person = (total_bill + (total_bill * tip_amount)) / people
print(f"Each person should pay: ${round(bill_per_person, 2)}")
