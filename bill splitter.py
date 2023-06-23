bill = float(input("what was the total bill\n"))
tip = int(input("what percentage of tip would you like to give\n"))
bill_split = int(input("how many people to split the bill?\n"))
tip_amount = bill*tip/100
pay_per_person = (bill + tip_amount)/bill_split
rounded_off_bill = round(pay_per_person,0)
rounded_off_bill = "{:.2f}".format(pay_per_person)
print(f"each person shoud pay {rounded_off_bill}")
     