##inputs
#Total rent 
rent = int(input("Enter your hostel/flat rent ="))
#Total food
food = int(input("Enter the amount of food order ="))
#Electricity units spend
electricity_spent = int(input("Enter the total of electricity spend ="))
#Charge per unit
charge_per_unit = int(input("Enter the charge per unit ="))
#persons living in hostel/flat
persons = int(input("Enter the number of persons living in hostel/flat =")) 

## Logic

#Total bill
total_bill = electricity_spent * charge_per_unit

#Total bill per person
output = (food + rent + total_bill) // persons

#Output
print("Each person will pay = ", output)