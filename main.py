print(" Welcome to the tip calculator! \n")
#If the bill was $150.00, split between 5 people, with 12% tip
bill = float(input("How much is the bill \n $"))
# The percentage that everyone want to tips
tip = int(input("How much tip do you want to give? 15, 18, 20, 22 \n %"))
# Number of peoples that will split the bill
people = int(input("How many people to split the bill? \n"))
# Caluculate the Total bill with tip
bill_with_tip = bill * (tip / 100) + bill
print(f"The total bill with tip is: \n ${bill_with_tip}")
# Caluculate  the total bill per person
bill_per_person = bill_with_tip / people
print(f"Each person should pay: \n ${bill_per_person}")
