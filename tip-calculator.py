# ask for the user for their total bill
user_total_bill = float(input("Enter your total bill:\n"))

# ask for the number of people willing to pay
no_of_people = int(input("how many people are paying?\n"))

# ask for the tip they are willing to pay in percent
tip_percent = float(input("Enter your tip in percent:\n"))

# calculate the tip actual amount
tip_amount = user_total_bill * (tip_percent / 100)

#calculate the total bill they are paying
total_bill = tip_amount + user_total_bill

#calculate each user bill
each_user_bill = total_bill / no_of_people
                                                     
# print out the result to the user in 2 decimal places
print(f"Each of you are to pay {each_user_bill: .2f}")