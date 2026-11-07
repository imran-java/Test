count = int(input("Please enter number of friends who will join the trip: "))
car_rental = float(input("Please enter the car rental fee: "))
accomodation_fee = float(input("Please enter the accomedatiom fee: "))
meals = []
total_meal = 0

total = car_rental + accomodation_fee
avg = total/count

for i in range (count):
    meal = float(input(f"Please enter total meal price for friend No{i + 1} for two days: "))
    meals.append(meal)
    total_meal += meal
    


for i in range(count):
    total_per_person = avg + meals[i]
    print (f"Friend no{i + 1} ows you RM {total_per_person}")

grand_total = total_meal + total
print (f"your grand total is RM {grand_total}")