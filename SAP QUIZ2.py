count = int(input("Please enter number of people who will join the trip: "))
car_rental = float(input("Please enter the car rental price: "))
accomodation_fee = float(input("Please enter the accomedatiom fee: "))
total_meal = 0

total = car_rental + accomodation_fee
avg = total/count

for i in range (count):
    meal = float(input(f"Please enter total meal price for person {i + 1} for two days: "))
    total_per_person = avg + meal
    print (f"Total value for friend {i + 1} is RM {total_per_person}\n")
    total_meal += meal

grand_total = total + total_meal
print (f"Your grand total for the trip is RM {grand_total}")
    


