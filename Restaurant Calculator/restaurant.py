import pyfiglet

display_calculator = "R e s t a u r a n t   C a l c u l a t o r"
print(pyfiglet.figlet_format(display_calculator))
bill = float(input("What was the total bill? "))
ask_tip = input("Would you like to tip? yes or no: ")
people = int(input("How many people to split the bill? "))
if ask_tip == "yes":
    tip = int(input("How much tip would you like to give? 10%, 12% or 15%? "))
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = "{:.2f}".format(bill_per_person)
    print(f"Each person should pay {final_amount}")
elif ask_tip == "no":
    total = "{:.2f}".format(bill / people)
    print(f"Each person should pay {total}")